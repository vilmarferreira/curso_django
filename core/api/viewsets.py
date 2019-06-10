from rest_framework.viewsets import ModelViewSet

from core.api.serializers import PessoaSerializer
from core.models import Pessoa


class PessoaViewSet(ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
