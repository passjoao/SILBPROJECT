from django.db import models


class Demands(models.Model):
    demands = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.demands