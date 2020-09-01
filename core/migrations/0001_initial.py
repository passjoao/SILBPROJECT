# Generated by Django 3.0.7 on 2020-07-24 22:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Captaincy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('initials', models.CharField(max_length=3)),
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
                ('scrivener', models.CharField(max_length=128)),
                ('generalRegisterMerces', models.BooleanField(default=False)),
                ('registerMeiasAnatas', models.BooleanField(default=False, verbose_name='Meias Anatas')),
                ('meiasAnatas', models.CharField(max_length=128, verbose_name='Valor Meias Anatas')),
                ('treasurerName', models.CharField(default='NA', max_length=128)),
                ('otherValue', models.CharField(max_length=128)),
                ('comments', models.CharField(default='NA', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Deferment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defered', models.BooleanField(default=True)),
                ('favorable', models.BooleanField(default=True)),
                ('scriviner', models.CharField(max_length=128)),
                ('dateRegister', models.DateField(default=datetime.date.today)),
                ('comments', models.TextField()),
                ('privileged_observations', models.TextField()),
                ('sources', models.TextField(verbose_name='Referência')),
                ('authority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authority', to='core.Authority')),
            ],
        ),
        migrations.CreateModel(
            name='Demands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demands', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(default='default.jpg', max_length=7, verbose_name='Referência')),
                ('file', models.FileField(default='default.jpg', upload_to='files/%Y/%m/%d', verbose_name='Arquivo')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(default='default.jpg', max_length=7, verbose_name='Referência')),
                ('foto', models.ImageField(default='defaltu.jpg', upload_to='images/%Y/%m/%d', verbose_name='Imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Justification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justification', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='LandRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=10, unique=True, verbose_name='Referência')),
                ('location', models.TextField(verbose_name='Localidade')),
                ('nearest_river', models.CharField(max_length=128, verbose_name='Ribeira')),
                ('hectare_area', models.FloatField(verbose_name='área em hectares')),
                ('published', models.BooleanField(default=False, verbose_name='Publicado')),
                ('landHistory', models.CharField(choices=[('SOLD', 'Comprada'), ('PRIMORDIAL', 'Primordial'), ('HERDED', 'Herdada'), ('VACANT', 'Devoluta nunca povoada'), ('ABANDONED', 'Devoluta por abandono'), ('RENTED', 'Aforada')], max_length=128, null=True, verbose_name='Histórico da terra')),
                ('land_record_type', models.CharField(choices=[('FARM', 'Fazenda'), ('MINING', 'Mineração')], max_length=128, verbose_name='Tipo de terra')),
                ('comments', models.TextField(default='')),
                ('captaincy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='land_records', to='core.Captaincy', verbose_name='Capitania')),
                ('limits', models.ManyToManyField(blank=True, related_name='_landrecord_limits_+', to='core.LandRecord', verbose_name='Limitantes')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('original_name', models.CharField(max_length=128)),
                ('spouse_name', models.CharField(max_length=128)),
                ('gender', models.CharField(choices=[('MALE', 'Homem'), ('FEMALE', 'Mulher'), ('NA', 'NA')], max_length=128)),
                ('indian', models.BooleanField(default=False)),
                ('captaincy_resident', models.BooleanField(default=True, verbose_name='Reside em capitania')),
                ('matrialStatus', models.CharField(choices=[('CASADO', 'Casado'), ('SOLTEIRO', 'Solteiro'), ('DIVORCIADO', 'Divorciado'), ('VIUVO', 'Viúvo')], default=[('CASADO', 'Casado'), ('SOLTEIRO', 'Solteiro'), ('DIVORCIADO', 'Divorciado'), ('VIUVO', 'Viúvo')], max_length=128)),
                ('secular_clergy', models.BooleanField(default=False)),
                ('regular_clergy', models.BooleanField(default=False)),
                ('comments', models.TextField()),
                ('privileged_observations', models.TextField()),
                ('captaincy_resident_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Capitania', to='core.Captaincy')),
            ],
        ),
        migrations.CreateModel(
            name='ReligiousOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Tramitations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pendingProvider', models.BooleanField(default=False, verbose_name='Passou por provedor/Procurador')),
                ('ProviderName', models.CharField(max_length=128, verbose_name='Nome provedor/Procurador')),
                ('pendingAssembly', models.BooleanField(default=False, verbose_name='Passou pela câmara ')),
                ('assemblyName', models.CharField(max_length=128, verbose_name='Nome camarário')),
                ('pendingScriviner', models.BooleanField(default=False, verbose_name='Passou por escrivão')),
                ('scrivinerName', models.CharField(max_length=128, verbose_name='Nome escrivão')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRequest', models.DateField()),
                ('same_measure', models.BooleanField(default=False)),
                ('requestType', models.CharField(choices=[('CONCESSION', 'Concessão'), ('REQUEST', 'Requisição'), ('CONFIRMATION', 'Confirmação')], max_length=128, verbose_name='Tipo de requisição')),
                ('comments', models.TextField(verbose_name='Observações')),
                ('privileged_observations', models.TextField(verbose_name='Observações privilegiada')),
                ('link', models.TextField(default='NA')),
                ('confirmation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request', to='core.Confirmation', verbose_name='Confirmação')),
                ('deferment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request', to='core.Deferment', verbose_name='Deferimento')),
                ('demands', models.ManyToManyField(to='core.Demands', verbose_name='Requisições')),
                ('files', models.ManyToManyField(to='core.Files', verbose_name='Arquivos')),
                ('justification', models.ManyToManyField(to='core.Justification', verbose_name='Justificativas')),
                ('medias', models.ManyToManyField(to='core.Image', verbose_name='Fotos')),
                ('owners', models.ManyToManyField(to='core.Owner', verbose_name='Sesmeiros')),
                ('record_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='request', to='core.LandRecord', verbose_name='Sesmaria')),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='religious_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owners', to='core.ReligiousOrder'),
        ),
        migrations.AddField(
            model_name='deferment',
            name='tramitations',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tramitations', to='core.Tramitations'),
        ),
    ]
