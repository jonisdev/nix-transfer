# Generated by Django 2.0.4 on 2018-05-01 20:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Criado em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transfer',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Deletado em'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Criado em'),
        ),
    ]
