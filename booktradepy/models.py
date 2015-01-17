from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    id = models.AutoField(primrary_key=True)
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    owner = models.ForeignKey('User')
    status = models.BooleanType()
    now_holds = models.ForeignKey('User')
    comment = models.CharField(max_length=512)

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey('User')
    receiver = models.ForeignKey('User')
    message = models.CharField(max_length=255)
