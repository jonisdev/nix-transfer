from django.db import models


class Transfer(models.Model):
    CC = 'CC'
    TED = 'TED'
    DOC = 'DOC'

    TYPE_CHOICES = (
        (CC, 'Conta Corrente'),
        (TED, 'Transfêrencia Eletrônica de Documentos'),
        (DOC, 'Documento de Ordem de Crédito'),
    )

    OK = 'OK'
    ERROR = 'ERROR'

    STATUS_CHOICES = (
        (OK, 'OK'),
        (ERROR, 'Erro'),
    )

    # TODO - Implement custom user
    user_id = models.IntegerField(
        verbose_name="ID do Usuário"
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


t = Transfer(user_id=222,
              paying_name ='Jonatan Vianna da Silva',
              paying_bank=1,
              paying_agency=3334,
              paying_account=188003,
              beneficiary_name='Jonatan Vianna da Silva',
              beneficiary_bank=1,
              beneficiary_agency=3334,
              beneficiary_account=188003,
              amount=9237651239872.97,
              type=Transfer.TYPE_CHOICES[0][1],
              status=Transfer.STATUS_CHOICES[0][0],
              )
