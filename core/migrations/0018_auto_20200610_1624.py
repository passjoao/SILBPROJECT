# Generated by Django 3.0.6 on 2020-06-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_deferment_record_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deferment',
            name='record_id',
        ),
        migrations.AlterField(
            model_name='tramitations',
            name='ProviderName',
            field=models.CharField(max_length=128, verbose_name='Nome provedor'),
        ),
        migrations.AlterField(
            model_name='tramitations',
            name='assemblyName',
            field=models.CharField(max_length=128, verbose_name='Nome camarário'),
        ),
        migrations.AlterField(
            model_name='tramitations',
            name='attorneyName',
            field=models.CharField(max_length=128, verbose_name='Nome procurador'),
        ),
        migrations.AlterField(
            model_name='tramitations',
            name='pendingAssembly',
            field=models.BooleanField(default=False, verbose_name='Passou pela câmara '),
        ),
        migrations.AlterField(
            model_name='tramitations',
            name='pendingAttorney',
            field=models.BooleanField(default=False, verbose_name='Passou por procurador'),
        ),
        migrations.AlterField(
            model_name='tramitations',
            name='pendingProvider',
            field=models.BooleanField(default=False, verbose_name='Passou por provedor'),
        ),
        migrations.AlterField(
            model_name='tramitations',
            name='pendingScriviner',
            field=models.BooleanField(default=False, verbose_name='Passou por escrivão'),
        ),
        migrations.AlterField(
            model_name='tramitations',
            name='scrivinerName',
            field=models.CharField(max_length=128, verbose_name='Nome escrivão'),
        ),
    ]
