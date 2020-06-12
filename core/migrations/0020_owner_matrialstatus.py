# Generated by Django 3.0.6 on 2020-06-10 19:34

import core.enum
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200610_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='matrialStatus',
            field=models.CharField(choices=[('CASADO', 'Casado'), ('SOLTEIRO', 'Solteiro'), ('DIVORCIADO', 'Divorciado'), ('VIUVO', 'Viúvo')], default=core.enum.MatrialStatus['SOLTEIRO'], max_length=128),
        ),
    ]
