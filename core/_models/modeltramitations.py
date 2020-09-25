from django.db import models


class Tramitations(models.Model):

    pendingProvider = models.BooleanField(default=False, verbose_name="Passou por provedor/Procurador")
    ProviderName = models.CharField(max_length=128, verbose_name="Nome provedor/Procurador", default="NA")

    pendingAssembly = models.BooleanField(default=False, verbose_name="Passou pela câmara")
    assemblyName = models.CharField(max_length=128, verbose_name="Nome camarário", default="NA")

    pendingScriviner = models.BooleanField(default=False, verbose_name="Passou por escrivão")
    scrivinerName = models.CharField(max_length=128, verbose_name="Nome escrivão", default="NA")

    def __str__(self):
        return str(self.id)