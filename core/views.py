from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView, ListView, DeleteView

from core.forms import PessoaForm
from core.models import Pessoa


class Index(TemplateView):
    template_name = 'core/index.html'


class PessoaCreateView(CreateView):
    model = Pessoa
    template_name = 'core/pessoa_create_view.html'
    form_class = PessoaForm

    def get_success_url(self):
        return reverse_lazy('core:pessoa_list')


class PessoaUpdateView(UpdateView):
    model = Pessoa
    template_name = 'core/pessoa_update_view.html'


class PessoaDetailView(DetailView):
    model = Pessoa
    template_name = 'core/pessoa_detail_view.html'


class PessoaListView(ListView):
    model = Pessoa
    template_name = 'core/pessoa_list_view.html'


class PessoaDeleteView(DeleteView):
    model = Pessoa
    template_name = 'core/pessoa_delete_view.html'

    def get_success_url(self):
        return reverse_lazy('core:pessoa_list')





# Create your views here.
