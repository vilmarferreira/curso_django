from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView

from contato.forms import ContatoForm
from contato.models import Contato


class ContatoCreateView(CreateView):
    model = Contato
    template_name = 'contato/contato_create_view.html'
    form_class = ContatoForm

    def get_success_url(self):
        return reverse_lazy('contato:contato_list')


class ContatoUpdateView(UpdateView):
    model = Contato
    template_name = 'contato/contato_update_view.html'
    form_class = ContatoForm

    def get_success_url(self):
        return reverse_lazy('contato:contato_list')

class ContatoDetailView(DetailView):
    model = Contato
    template_name = 'contato/contato_detail_view.html'


class ContatoListView(ListView):
    model = Contato
    template_name = 'contato/contato_list_view.html'


class ContatoDeleteView(DeleteView):
    model = Contato
    template_name = 'contato/contato_delete_view.html'

    def get_success_url(self):
        return reverse_lazy('contato:contato_list')

# Create your views here.
