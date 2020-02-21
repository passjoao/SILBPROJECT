from django.db import models
from django.contrib.auth import get_user_model


class Log(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True
    )
    event_description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
