from django.db import models


class Image(models.Model):
    reference = models.CharField(default="default.jpg", max_length=7,verbose_name=u"Referência")
    foto = models.ImageField(default="defaltu.jpg", upload_to="images/%Y/%m/%d", verbose_name=u"Imagem")

    def __str__(self):
        return self.reference