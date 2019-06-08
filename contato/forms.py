from django.forms import ModelForm

from contato.models import Contato


class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'