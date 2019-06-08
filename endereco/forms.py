from django.forms import ModelForm

from endereco.models import Endereco


class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'