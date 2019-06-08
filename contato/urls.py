from django.urls import path

from contato.views import ContatoCreateView, ContatoUpdateView, ContatoDetailView, ContatoDeleteView, ContatoListView

app_name = 'contato'

urlpatterns = [
    path('create/', ContatoCreateView.as_view(), name='contato_create'),
    path('list/', ContatoListView.as_view(), name='contato_list'),
    path('update/<int:pk>', ContatoUpdateView.as_view(), name='contato_update'),
    path('detail/<int:pk>', ContatoDetailView.as_view(), name='contato_detail'),
    path('delete/<int:pk>', ContatoDeleteView.as_view(), name='contato_delete'),
]