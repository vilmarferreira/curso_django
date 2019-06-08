from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView

from endereco.forms import EnderecoForm
from endereco.models import Endereco


class EnderecoCreateView(CreateView):
    model = Endereco
    template_name = 'endereco/endereco_create_view.html'
    form_class = EnderecoForm

    def get_success_url(self):
        return reverse_lazy('endereco:endereco_list')


class EnderecoListView(ListView):
    model = Endereco
    template_name = 'endereco/endereco_list_view.html'


class EnderecoDetailView(DetailView):
    model = Endereco
    template_name = 'endereco/endereco_detail_view.html'


class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = 'endereco/endereco_delete_view.html'

    def get_success_url(self):
        return reverse_lazy('endereco:endereco_list')



# Create your views here.
