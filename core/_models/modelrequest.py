from django.db import models
from django.urls import reverse

from core._models.modelconfirmation import Confirmation
from core._models.modeldeferment import Deferment
from core._models.modeldemands import Demands
from core._models.modelfiles import Files
from core._models.modelimage import Image
from core._models.modeljustification import Justification
from core._models.modellandrecord import LandRecord
from core._models.modelowner import Owner
from core.enum import RequestType



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
    comments = models.TextField(verbose_name='Observações')
    privileged_observations = models.TextField(verbose_name='Observações privilegiada')
    link = models.TextField(default="NA")
    deferment = models.ForeignKey(
        Deferment, on_delete=models.SET_NULL, related_name='request', null=True, verbose_name='Deferimento'
    )
    confirmation = models.ForeignKey(
        Confirmation, on_delete=models.SET_NULL, related_name='request', null=True, verbose_name='Confirmação'
    )

    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('request-detail', args=[str(self.id)])

    def __str__(self):
        return self.record_id.reference