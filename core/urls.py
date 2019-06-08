from django.urls import path

from core.views import PessoaCreateView

app_name = 'core'

urlpatterns = [
    path('PessoaCreateView/', PessoaCreateView.as_view(), name='pessoa_create_view')


]