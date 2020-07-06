from django.db import models
from django.urls import reverse

from core._models.modelcaptaincy import Captaincy
from core._models.modelreligiousorder import *
from core.enum import MatrialStatus, Gender


class Owner(models.Model):
    name = models.CharField(max_length=128)
    original_name = models.CharField(max_length=128)
    spouse_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=128, choices=Gender.choices())
    indian = models.BooleanField(default=False)
    captaincy_resident = models.BooleanField(default=True, verbose_name="Reside em capitania")
    captaincy_resident_name =models.ForeignKey(
        Captaincy, on_delete=models.SET_NULL, null=True,
        related_name='Capitania'
    )
    matrialStatus = models.CharField(max_length=128, choices=MatrialStatus.choices(), default=MatrialStatus.choices())
    secular_clergy = models.BooleanField(default=False)
    regular_clergy = models.BooleanField(default=False)
    comments = models.TextField()
    privileged_observations = models.TextField()
    religious_order = models.ForeignKey(
        ReligiousOrder, on_delete=models.SET_NULL, null=True,
        related_name='owners'
    )

    def __str__(self):
        return '%s' %(self.name)


    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('owner-detail', args=[str(self.name)])