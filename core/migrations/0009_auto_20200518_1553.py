# Generated by Django 3.0.6 on 2020-05-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200417_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='dateConcession',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='dateRequest',
            field=models.DateField(auto_now=True),
        ),
    ]