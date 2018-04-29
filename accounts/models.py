from django.db import models
from django.core.exceptions import ValidationError
from brazilnum.cnpj import validate_cnpj
# Create your models here.

from django.contrib.auth.models import (
    AbstractBaseUser, UserManager)


def validate_br_cnpj(value):
    if not validate_cnpj(value):
        raise ValidationError("%(value)s não é um CNPJ válido")


class User(AbstractBaseUser):
    name = models.CharField(
        verbose_name='Nome',
        max_length=128,
    )
    cnpj = models.CharField(
        verbose_name='CNPJ',
        max_length=14,
        validators=[validate_br_cnpj],
        help_text='O CNPJ deve ter 14 numeros e ser válido.',
        error_messages={'invalid': 'O CNPJ deve ter 14 numeros e ser válido.'},
        unique=True
    )

    is_active = models.BooleanField(
        verbose_name='Usuario ativo?',
        default=True
    )

    created_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        verbose_name='Criado em',
        auto_now=True
    )

    objects = UserManager()

    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'cnpj'

    def __str__(self):
        return self.name and self.cnpj
