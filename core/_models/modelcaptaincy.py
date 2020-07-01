from django.db import models


class Captaincy(models.Model):
    name = models.CharField(max_length=128)
    initials = models.CharField(max_length=3)

    def __str__(self):
        return self.name