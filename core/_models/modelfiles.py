from django.db import models


class Files(models.Model):
    
    file = models.FileField(default="default.jpg", upload_to="files/%Y/%m/%d", verbose_name=u"Arquivo")

    def __str__(self):
        return str(self.id)