# Generated by Django 3.0.7 on 2020-09-21 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='confirmation',
        ),
        migrations.AddField(
            model_name='confirmation',
            name='request_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request', to='core.Request', verbose_name='Carta de requisição'),
        ),
    ]
