# Generated by Django 3.0.7 on 2020-09-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200921_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authority',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
