from rest_framework import routers

from contato.api.viewsets import ContatoViewSet
from core.api.viewsets import PessoaViewSet
from endereco.api.viewsets import EnderecoViewSet

router = routers.DefaultRouter()


router.register(r'pessoa',PessoaViewSet)
router.register(r'contato',ContatoViewSet)
router.register(r'endereco',EnderecoViewSet)