from django.db import models
from django.urls import reverse
import datetime
from core._models.modelrequest import Request


class Confirmation(models.Model): #Classe que define se a carta foi confirmada
    confirmationReference = models.CharField(default="", max_length=128)
    dateConfirmation = models.DateField(verbose_name="Data de Confirmação", default=datetime.date.today)
    confirmationLisbon = models.BooleanField(default=True) #se a carta foi confirmada em Lisboa
    confirmationPresential = models.BooleanField(default=True) #se o requerimento da confirmação está presentena carta
    concessionPresential = models.BooleanField(default=True) #se o requerimento da concessão está presente na carta
    concessionEqual = models.BooleanField(default=True) #caso tenha mais de um sesmeiro para a terra, a divissão dela foi de forma igualitária
    kingName = models.CharField(max_length=128) #nomde do rei que aprovou a cooncessão e a confirmação
    treasurerName = models.CharField(max_length=128, default="NA") #nome do tesoureiro do registro da carta
    scrivener = models.CharField(max_length=128) #escrivão da carta de confirmaçao
    register = models.CharField(max_length=512, default="NA")
    registerMeiasAnatas = models.BooleanField(default=False, verbose_name="Meias Anatas")
    meiasAnatas = models.CharField(max_length=128, verbose_name='Valor Meias Anatas') #um imposto cobrado pela carta
    otherValue = models.CharField(max_length=128) #outros valores cobrados
    comments = models.CharField(max_length=128, default="NA")
    request_id = models.ForeignKey(
        Request, on_delete=models.SET_NULL, related_name='request', null=True, verbose_name='Carta de requisição'
    )
    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('confirmation-detail', args=[str(self.id)])

    def save(self, *args, **kwargs): 
        self.confirmationReference = ('CF ' + self.request_id.reference)
        super(Confirmation, self).save(*args, **kwargs) 