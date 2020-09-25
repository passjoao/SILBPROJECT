from django.db import models


class Image(models.Model):
    foto = models.ImageField(default="defaltu.jpg", upload_to="images/%Y/%m/%d", verbose_name=u"Imagem")

    def __str__(self):
        return str(self.id)