import datetime

from django.db import models

from core._models.modelauthority import Authority


class Deferment(models.Model):#classe pada parte de deferimento da carta e tramitações
    defered = models.BooleanField(default=True)
    favorable = models.BooleanField(default=True)#se a concessão foi favorável
    scriviner = models.CharField(max_length=128)#escrivão do documento de deferimento
    dateRegister = models.DateField(default=datetime.date.today)
    comments = models.TextField()
    privileged_observations = models.TextField()
    sources = models.TextField(verbose_name="Fonte")#referencia do documento físico
    authority = models.ForeignKey(
        Authority, on_delete=models.SET_NULL, related_name='authority', null = True
    )
    tramitations = models.ForeignKey(
        'Tramitations', on_delete=models.SET_NULL, related_name='tramitations', null=True
    )

    def __str__(self):
        return str(self.id)



    def get_absolute_url(self):
        """Retorna a url para acessar uma instancia específica de MyModelName."""
        return reverse('deferment-detail', args=[str(self.id)])