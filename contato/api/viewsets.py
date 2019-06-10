from rest_framework.viewsets import ModelViewSet
from contato.models import Contato
from .serializers import ContatoSerializer



class ContatoViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
