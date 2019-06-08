from django.db import models
from endereco.models import Endereco
from contato.models import Contato


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    contato = models.ForeignKey(Contato,on_delete=models.PROTECT)


# Create your models here.
