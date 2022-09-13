from django.db import models
from django.conf import settings


class Link(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True)
    original_link = models.URLField()
    tag = models.CharField(max_length=255,unique=True)
    visits = models.PositiveIntegerField(default=0)