from django.db import models


class Files(models.Model):
    reference = models.CharField(default="default.jpg", max_length=7, verbose_name=u"Referência")
    file = models.FileField(default="default.jpg", upload_to="files/%Y/%m/%d", verbose_name=u"Arquivo")

    def __str__(self):
        return self.reference