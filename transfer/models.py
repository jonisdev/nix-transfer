from django.db import models
from model_utils import Choices
from datetime import datetime as dt
from django.conf import settings

class Transfer(models.Model):
    # CC = 'CC'
    # TED = 'TED'
    # DOC = 'DOC'

    TYPE_CHOICES = Choices(
        ('CC', 'Conta Corrente'),
        ('TED', 'Transfêrencia Eletrônica de Documentos'),
        ('DOC', 'Documento de Ordem de Crédito'),
    )

    # OK = 'OK'
    # ERROR = 'ERROR'

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
    paying_name = models.CharField(
        verbose_name="Nome do Pagador",
        max_length=128

    )
    paying_bank = models.CharField(
        verbose_name="Banco do Pagador",
        max_length=3
    )
    paying_agency = models.CharField(
        verbose_name="Agência do Pagador",
        max_length=4
    )
    paying_account = models.CharField(
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

        if self.paying_bank == self.beneficiary_bank:
            self.type = self.TYPE_CHOICES.CC
            self.save()
        elif dt.weekday(current_datetime) in (5, 6):
            self.type = self.TYPE_CHOICES.DOC
            self.save()
        elif current_time > initial_ted_time and \
                current_time < final_ted_time and \
                self.amount < 5000.0:
            self.type = self.TYPE_CHOICES.TED
            self.save()
        else:
            self.type = self.TYPE_CHOICES.DOC
            self.save()

    def set_transfer_status(self):
        if self.amount > 100000.0:
            self.status = self.STATUS_CHOICES.ERROR
            self.save()
        else:
            self.status = self.STATUS_CHOICES.OK
            self.save()


from accounts.models import User
u = User(name='Brazil Exportations HUE BR', cnpj=31415850000508)


# from transfer.models import Transfer
# t = Transfer(user_id=222,
#               paying_name ='Jonatan Vianna da Silva',
#               paying_bank=1,
#               paying_agency=3334,
#               paying_account=188003,
#               beneficiary_name='Jonatan Vianna da Silva',
#               beneficiary_bank=1,
#               beneficiary_agency=3334,
#               beneficiary_account=188003,
#               amount=9237651239872.97,
#               )
