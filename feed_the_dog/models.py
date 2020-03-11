from django.db import models
from django.conf import settings

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    who = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    where = models.CharField("the address the user made the request from", max_length=250)

class Dog(models.Model):
    name = models.CharField("name of the dog!", max_length=250)
    owners = models.ManyToManyField(settings.AUTH_USER_MODEL)
