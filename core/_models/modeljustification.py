from django.db import models


class Justification(models.Model):
    justification = models.CharField(max_length=512, blank=True)

    def __str__(self):
        return self.justification