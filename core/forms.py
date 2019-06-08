from django.forms import ModelForm

from core.models import Pessoa


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'