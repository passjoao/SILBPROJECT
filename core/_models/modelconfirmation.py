from django.db import models
from django.urls import reverse


class Confirmation(models.Model): #Classe que define se a carta foi confirmada
    dateConfirmation = models.DateField(verbose_name="Data de Confirmação")
    dateConcession = models.DateField(verbose_name="Data de concessão")
    confirmationLisbon = models.BooleanField(default=True) #se a carta foi confirmada em Lisboa
    concessionPresential = models.BooleanField(default=True) #se a concessão foi presencial
    concessionEqual = models.BooleanField(default=True) #caso tenha mais de um sesmeiro para a terra, a divissão dela foi de forma igualitária
    kingName = models.CharField(max_length=128) #nomde do rei que aprovou a cooncessão e a confirmação
    treasurerName = models.CharField(max_length=128) #nome do tesoureiro do registro da carta
    scrivener = models.CharField(max_length=128) #escrivão da carta de confirmaçao
    generalRegisterMerces = models.BooleanField(default=False)
    registerMeiasAnatas = models.BooleanField(default=False, verbose_name="Meias Anatas")
    meiasAnatas = models.CharField(max_length=128, verbose_name='Valor Meias Anatas') #um imposto cobrado pela carta
    treasurerName = models.CharField(max_length=128, default='NA')
    otherValue = models.CharField(max_length=128) #outros valores cobrados
    comments = models.CharField(max_length=128, default="NA")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('confirmation-detail', args=[str(self.id)])