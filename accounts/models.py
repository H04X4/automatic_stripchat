from django.db import models

class Account(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
