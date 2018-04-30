from django.db import models
from model_utils import Choices
from datetime import datetime as dt
from django.conf import settings


class Transfer(models.Model):
    MAX_TRANSFER_AMOUNT = 100000.0
    MIN_TRANSFER_AMOUNT = 0.0
    MAX_TED_TRANSFER_AMOUNT = 5000.0
    TYPE_CHOICES = Choices(
        ('CC', 'Conta Corrente'),
        ('TED', 'Transfêrencia Eletrônica de Documentos'),
        ('DOC', 'Documento de Ordem de Crédito'),
    )

    STATUS_CHOICES = Choices(
        ('OK', 'OK'),
        ('ERROR', 'Erro'),
    )

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='User',
        related_name='transfers',
        on_delete=models.CASCADE
    )
    payer_name = models.CharField(
        verbose_name="Nome do Pagador",
        max_length=128

    )
    payer_bank = models.CharField(
        verbose_name="Banco do Pagador",
        max_length=3
    )
    payer_agency = models.CharField(
        verbose_name="Agência do Pagador",
        max_length=4
    )
    payer_account = models.CharField(
        verbose_name="Conta do Pagador",
        max_length=6
    )
    beneficiary_name = models.CharField(
        verbose_name="Nome do Beneficiário",
        max_length=128
    )
    beneficiary_bank = models.CharField(
        verbose_name="Banco do Beneficiário",
        max_length=3
    )
    beneficiary_agency = models.CharField(
        verbose_name="Agência do Beneficiário",
        max_length=4
    )
    beneficiary_account = models.CharField(
        verbose_name="Conta do Beneficiário",
        max_length=6
    )
    # 9.123.123.123.123,00
    amount = models.DecimalField(
        verbose_name="Valor",
        max_digits=15,
        decimal_places=2,
    )
    type = models.CharField(
        verbose_name="Tipo",
        max_length=4,
        choices=TYPE_CHOICES,
    )
    status = models.CharField(
        verbose_name='Status',
        max_length=12,
        choices=STATUS_CHOICES
    )

    def set_transfer_type(self):
        current_datetime = dt.now()
        current_time = dt.time(current_datetime)
        current_date = current_datetime.date()
        initial_ted_time = dt.time(dt(
            current_date.year, current_date.month, current_date.day, 10, 0, 0))
        final_ted_time = dt.time(dt(
            current_date.year, current_date.month, current_date.day, 16, 0, 0))

        if self.payer_bank == self.beneficiary_bank:
            self.type = self.TYPE_CHOICES.CC
        elif dt.weekday(current_datetime) in (5, 6):
            self.type = self.TYPE_CHOICES.DOC
        elif initial_ted_time < current_time < final_ted_time and \
                self.amount < self.MAX_TED_TRANSFER_AMOUNT:
            self.type = self.TYPE_CHOICES.TED
        else:
            self.type = self.TYPE_CHOICES.DOC

    def set_transfer_status(self):
        if self.MAX_TRANSFER_AMOUNT > self.amount >= self.MIN_TRANSFER_AMOUNT:
            self.status = self.STATUS_CHOICES.OK
        else:
            self.status = self.STATUS_CHOICES.ERROR

    def __repr__(self):
        return self.payer_name

    def save(self, *args, **kwargs):
        self.set_transfer_type()
        self.set_transfer_status()
        super(Transfer, self).save(*args, **kwargs)
