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
    date = models.DateField()
    same_measure = models.BooleanField(default=False)
    comments = models.TextField()
    privileged_observations = models.TextField()
    requestType = models.CharField(choices=RequestType.choices())
    record_id = models.ForeignKey(
        LandRecord, on_delete=models.SET_NULL, related_name='request'
    )
    justification = models.ManyToManyField(Justification)