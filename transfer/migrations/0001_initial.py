# Generated by Django 2.0.4 on 2018-04-30 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payer_name', models.CharField(max_length=128, verbose_name='Nome do Pagador')),
                ('payer_bank', models.CharField(max_length=3, verbose_name='Banco do Pagador')),
                ('payer_agency', models.CharField(max_length=4, verbose_name='Agência do Pagador')),
                ('payer_account', models.CharField(max_length=6, verbose_name='Conta do Pagador')),
                ('beneficiary_name', models.CharField(max_length=128, verbose_name='Nome do Beneficiário')),
                ('beneficiary_bank', models.CharField(max_length=3, verbose_name='Banco do Beneficiário')),
                ('beneficiary_agency', models.CharField(max_length=4, verbose_name='Agência do Beneficiário')),
                ('beneficiary_account', models.CharField(max_length=6, verbose_name='Conta do Beneficiário')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Valor')),
                ('type', models.CharField(choices=[('CC', 'Conta Corrente'), ('TED', 'Transfêrencia Eletrônica de Documentos'), ('DOC', 'Documento de Ordem de Crédito')], max_length=4, verbose_name='Tipo')),
                ('status', models.CharField(choices=[('OK', 'OK'), ('ERROR', 'Erro')], max_length=12, verbose_name='Status')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transfers', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]