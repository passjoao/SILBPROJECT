# Generated by Django 3.0.6 on 2020-06-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_landrecord_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='link',
            field=models.TextField(default='NA'),
        ),
    ]
