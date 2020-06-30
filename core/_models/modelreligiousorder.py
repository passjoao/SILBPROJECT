from django.db import models

class ReligiousOrder(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return '%s' %(self.name)