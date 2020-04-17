from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from core.enum import Gender, LandRecordType, LandHistory, RequestType, Titles


class ReligiousOrder(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name


class Owner(models.Model):
    name = models.CharField(max_length=128)
    original_name = models.CharField(max_length=128)
    spouse_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=128, choices=Gender.choices())
    indian = models.BooleanField(default=False)
    captaincy_resident = models.BooleanField(default=True)
    secular_clergy = models.BooleanField(default=False)
    regular_clergy = models.BooleanField(default=False)
    comments = models.TextField()
    privileged_observations = models.TextField()
    religious_order = models.ForeignKey(
        ReligiousOrder, on_delete=models.SET_NULL, null=True,
        related_name='owners'
    )

    def __str__(self):
        return self.name

    class meta:
        ordering = ['name']


    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('owner-detail', args=[str(self.name)])


class Captaincy(models.Model):
    name = models.CharField(max_length=128)
    initials = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class LandRecord(models.Model):
    reference = models.CharField(max_length=10, unique=True)
    location = models.TextField()
    nearest_river = models.CharField(max_length=128, null=False)
    hectare_area = models.FloatField()
    published = models.BooleanField(default=False)
    landHistory = models.CharField(max_length=128, choices=LandHistory.choices(), null=True)
    land_record_type = models.CharField(
        max_length=128, choices=LandRecordType.choices()
    )
    captaincy = models.ForeignKey(
        Captaincy, on_delete=models.CASCADE, related_name='land_records'
    )
    limits = models.ManyToManyField(
        'self', blank=True, related_name='limits'
    )

    class meta:
        ordering = ['reference']


    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('pesqusia-detail', args=[str(self.reference)])

    def __str__(self):
        return self.reference


class Justification(models.Model):
    justification = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.justification


class Demands(models.Model):
    demands = models.CharField(max_length=128, blank=True)
    
    def __str__(self):
        return self.demands
class Files(models.Model):
    reference = models.CharField(default="default.jpg", max_length=7, verbose_name=u"Referência")
    file = models.FileField(default="default.jpg", upload_to="files/%Y/%m/%d", verbose_name=u"Arquivo")

    def __str__(self):
        return self.reference


class Image(models.Model):
    reference = models.CharField(default="default.jpg", max_length=7,verbose_name=u"Referência")
    foto = models.ImageField(default="defaltu.jpg", upload_to="images/%Y/%m/%d", verbose_name=u"Imagem")

    def __str__(self):
        return self.reference   


class Request(models.Model):
    dateRequest = models.DateField()
    same_measure = models.BooleanField(default=False)
    requestType = models.CharField(
        max_length=128, choices=RequestType.choices(), verbose_name='Tipo de requisição'
    )
    record_id = models.ForeignKey(
        LandRecord, on_delete=models.SET_NULL, related_name='request', null=True, verbose_name='Sesmaria'
    )
    medias = models.ManyToManyField(
        Image, verbose_name="Fotos"
    )
    files = models.ManyToManyField(
        Files, verbose_name="Arquivos"
    )
    owners = models.ManyToManyField(Owner, verbose_name='Sesmeiros')
    justification = models.ManyToManyField(Justification, verbose_name='Justificativas')
    demands = models.ManyToManyField(Demands, verbose_name='Requisições')
    comments = models.TextField(verbose_name='observações')
    privileged_observations = models.TextField(verbose_name='observações privilegiada')

    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('request-detail', args=[str(self.id)])

    def __str__(self):
        return self.record_id.reference




class Confirmation(models.Model): #Classe que define se a carta foi confirmada
    dateConfirmation = models.DateField()
    confirmationLisbon = models.BooleanField(default=True) #se a carta foi confirmada em Lisboa
    concessionPresential = models.BooleanField(default=True) #se a concessão foi presencial
    concessionEqual = models.BooleanField(default=True) #caso tenha mais de um sesmeiro para a terra, a divissão dela foi de forma igualitária
    kingName = models.CharField(max_length=128) #nomde do rei que aprovou a cooncessão e a confirmação
    treasurerName = models.CharField(max_length=128) #nome do tesoureiro do registro da carta
    scrivener = models.CharField(max_length=128) #escrivão da carta de confirmaçao
    meiasAnatas = models.CharField(max_length=128) #um imposto cobrado pela carta
    otherValue = models.CharField(max_length=128) #outros valores cobrados

    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('confirmation-detail', args=[str(self.id)])



class Authority(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128, choices=Titles.choices())

    def __str__(self):
        return self.name


class Deferment(models.Model):#classe pada parte de deferimento da carta e tramitações
    defered = models.BooleanField(default=True)
    favorable = models.BooleanField(default=True)#se a concessão foi favorável
    scriviner = models.CharField(max_length=128)#escrivão do documento de deferimento
    comments = models.TextField()
    privileged_observations = models.TextField()
    sources = models.TextField()#referencia do documento físico
    authority = models.ForeignKey(
        Authority, on_delete=models.SET_NULL, related_name='authority', null = True
    )
    record_id = models.ForeignKey(
        LandRecord, on_delete=models.SET_NULL, related_name='request_Deferment', null=True
    )
    tramitations = models.ForeignKey(
        'Tramitations', on_delete=models.SET_NULL, related_name='tramitations', null=True
    )

    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('deferment-detail', args=[str(self.id)])



class Tramitations(models.Model):
    pendingProvider = models.BooleanField(default=False)
    ProviderName = models.CharField(max_length=128)

    pendingAttorney = models.BooleanField(default=False)
    attorneyName = models.CharField(max_length=128)
    
    pendingAssembly = models.BooleanField(default=False)
    assemblyName = models.CharField(max_length=128)
    
    pendingScriviner = models.BooleanField(default=False)
    scrivinerName = models.CharField(max_length=128)


 