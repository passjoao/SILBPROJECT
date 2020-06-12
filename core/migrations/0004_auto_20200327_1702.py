# Generated by Django 2.2.4 on 2020-03-27 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200221_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('title', models.CharField(choices=[('CAPITAOMOR', 'CAPITAO-MOR'), ('GORVERNADOR', 'GORVERNADOR'), ('GORVERNADORGERAL', 'GORVERNADOR GERAL'), ('CAPITAO', 'CAPITAO'), ('VICEREI', 'VICE REI'), ('CAMARA', 'CÂMARA'), ('TRIUNVIRATO', 'TRIUNVIRATO'), ('PRESIDENTEPROVINCIAL', 'PRESIDENTE PROVINCIAL'), ('CAPITAOLOCOTENENTE', 'CAPITAO LOCO TENENTE')], max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateConfirmation', models.DateField()),
                ('confirmationLisbon', models.BooleanField(default=True)),
                ('concessionPresential', models.BooleanField(default=True)),
                ('concessionEqual', models.BooleanField(default=True)),
                ('kingName', models.CharField(max_length=128)),
                ('treasurerName', models.CharField(max_length=128)),
                ('scrivener', models.CharField(max_length=128)),
                ('meiasAnatas', models.CharField(max_length=128)),
                ('otherValue', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Justification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justification', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Tramitations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pendingProvider', models.BooleanField(default=False)),
                ('ProviderName', models.CharField(max_length=128)),
                ('pendingAttorney', models.BooleanField(default=False)),
                ('attorneyName', models.CharField(max_length=128)),
                ('pendingAssembly', models.BooleanField(default=False)),
                ('assemblyName', models.CharField(max_length=128)),
                ('pendingScriviner', models.BooleanField(default=False)),
                ('scrivinerName', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='landrecord',
            name='landHistory',
            field=models.CharField(choices=[('SOLD', 'SOLD'), ('PRIMORDIAL', 'PRIMORDIAL'), ('VACANT', 'VACANT'), ('AFORADA', 'AFORADA')], max_length=128, null=True),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRequest', models.DateField()),
                ('same_measure', models.BooleanField(default=False)),
                ('comments', models.TextField()),
                ('privileged_observations', models.TextField()),
                ('requestType', models.CharField(choices=[('CONCESSION', 'CONCESSION'), ('REQUEST', 'REQUEST'), ('CONFIRMATION', 'CONFIRMATION')], max_length=128)),
                ('justification', models.ManyToManyField(to='core.Justification')),
                ('record_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request', to='core.LandRecord')),
            ],
        ),
        migrations.CreateModel(
            name='Deferment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defered', models.BooleanField(default=True)),
                ('favorable', models.BooleanField(default=True)),
                ('scriviner', models.CharField(max_length=128)),
                ('comments', models.TextField()),
                ('privileged_observations', models.TextField()),
                ('sources', models.TextField()),
                ('authority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authority', to='core.Authority')),
                ('record_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request_Deferment', to='core.LandRecord')),
                ('tramitations', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tramitations', to='core.Tramitations')),
            ],
        ),
    ]