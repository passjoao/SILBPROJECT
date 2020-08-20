from django.db import models
from django.urls import reverse

from core._models.modelcaptaincy import Captaincy
from core.enum import LandHistory, LandRecordType


class LandRecord(models.Model):
    reference = models.CharField(max_length=10, unique=True, verbose_name="Referência", blank=True, null=True)
    oldReference = models.CharField(max_length=10, unique=True, verbose_name="Referência da SILB antiga", default="")
    location = models.TextField(verbose_name="Localidade")
    nearest_river = models.CharField(max_length=128, null=False, verbose_name="Ribeira")
    hectare_area = models.FloatField(verbose_name="área em hectares")
    #comprimento
    #largura
    
    landHistory = models.CharField(max_length=128, choices=LandHistory.choices(), null=True, verbose_name="Histórico da terra")
    comments = models.TextField(default="")
    captaincy = models.ForeignKey(
        Captaincy, on_delete=models.CASCADE, related_name='land_records', verbose_name="Capitania"
    )
    limits = models.ManyToManyField(
        'self', blank=True, related_name='limits',
        verbose_name="Limitantes"
    )
    published = models.BooleanField(default=False, verbose_name="Publicar")

    class meta:
        ordering = ['reference']


    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('pesqusia-detail', args=[str(self.reference)])

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        capitania = self.captaincy.initials
        self.reference = capitania
        super(LandRecord, self).save(*args, **kwargs)
