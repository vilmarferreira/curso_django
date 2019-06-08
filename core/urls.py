from django.urls import path

from core.views import Index, PessoaCreateView, PessoaListView, PessoaUpdateView, PessoaDeleteView, PessoaDetailView

app_name = 'core'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('new/', PessoaCreateView.as_view(), name='pessoa_create'),
    path('list/', PessoaListView.as_view(), name='pessoa_list'),
    path('update/<int:pk>', PessoaUpdateView.as_view(), name='pessoa_update'),
    path('delete/<int:pk>', PessoaDeleteView.as_view(), name='pessoa_delete'),
    path('detail/<int:pk>', PessoaDetailView.as_view(), name='pessoa_detail'),



]