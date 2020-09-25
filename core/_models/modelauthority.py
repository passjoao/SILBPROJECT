from django.db import models
from core.enum import Titles


class Authority(models.Model):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

    def __str__(self):
        return '%s' %(self.name)