from django.db import models

class Endereco(models.Model):
    logradouro = models.CharField(max_length=80, null=True, blank=False)
    bairro = models.CharField(max_length=30, null=True, blank=False)
    estado = models.CharField(max_length=30, null=True, blank=False)
    municipio = models.CharField(max_length=30, null=True, blank=False)

    def __str__(self):
        return '{}-{}'.format(self.logradouro, self.bairro)

# Create your models here.
