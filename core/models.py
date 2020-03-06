from django.db import models

from core.enum import Gender, LandRecordType, LandHistory, RequestType


class ReligiousOrder(models.Model):
    name = models.CharField(max_length=128)


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


class Captaincy(models.Model):
    name = models.CharField(max_length=128)
    initials = models.CharField(max_length=3)


class LandRecord(models.Model):
    reference = models.CharField(max_length=10, unique=True)
    location = models.TextField()
    nearest_river = models.CharField(max_length=128, null=False)
    hectare_area = models.FloatField()
    published = models.BooleanField(default=False)
    landHistory = models.CharField(max_length=128, choices=LandHistory.choices())
    land_record_type = models.CharField(
        max_length=128, choices=LandRecordType.choices()
    )
    captaincy = models.ForeignKey(
        Captaincy, on_delete=models.CASCADE, related_name='land_records'
    )
    limits = models.ManyToManyField(
        'self', blank=True, related_name='limits'
    )


class Justification(models.Model):
    justification = models.CharField(max_length=128)


class Request(models.Model):
    dateRequest = models.DateField()
    same_measure = models.BooleanField(default=False)
    comments = models.TextField()
    privileged_observations = models.TextField()
    requestType = models.CharField(choices=RequestType.choices())
    record_id = models.ForeignKey(
        LandRecord, on_delete=models.SET_NULL, related_name='request'
    )
    justification = models.ManyToManyField(Justification)

class Confirmation(models.Model): #prate mais burocrática 
    dateConfirmation = models.DateField()
    confirmationLisbon = models.BooleanField(default=True) #se a carta foi confirmada em Lisboa
    concessionPresential = models.BooleanField(default=True) #se a concessão foi presencial
    concessionEqual = models.BooleanField(default=True) #caso tenha mais de um sesmeiro para a terra, a divissão dela foi de forma igualitária
    kingName = models.CharField(max_length=128) #nomde do rei que aprovou a cooncessão e a confirmação
    tearsuryName = models.CharField(max_length=128) #nome do tesoureiro do registro da carta
    scrivener = models.CharField(max_length=128) #escrivão da carta
    meiasAnatas = models.CharField(max_length=128) #um imposto cobrado pela carta
    otherValue = models.CharField(max_length=128) #outros valores cobrados
