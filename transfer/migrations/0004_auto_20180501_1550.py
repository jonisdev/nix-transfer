# Generated by Django 2.0.4 on 2018-05-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0003_auto_20180501_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Deletado em'),
        ),
    ]