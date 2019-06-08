from django.db import models
from endereco.models import Endereco
from contato.models import Contato


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=False)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT)
    contato = models.ForeignKey(Contato,on_delete=models.PROTECT)

    def __str__(self):
        return '{}-{}-{}'.format(self.nome, self.endereco.logradouro, self.contato.telefone_1)

# Create your models here.
