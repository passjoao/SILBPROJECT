# Generated by Django 3.0.6 on 2020-06-10 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_request_confirmation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deferment',
            name='record_id',
        ),
        migrations.AddField(
            model_name='deferment',
            name='dateRegister',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
