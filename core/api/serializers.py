from rest_framework.serializers import ModelSerializer

from contato.api.serializers import ContatoSerializer
from core.models import Pessoa
from endereco.api.serializers import EnderecoSerializer


class PessoaSerializer(ModelSerializer):
    endereco = EnderecoSerializer()
    contato = ContatoSerializer()
    class Meta:
        model = Pessoa
        fields = '__all__'