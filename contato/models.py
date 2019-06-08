from django.db import models

class Contato(models.Model):
    telefone_1 = models.CharField(max_length=13)
    telefone_2 = models.CharField(max_length=13)
    email = models.CharField(max_length=100)

# Create your models here.
