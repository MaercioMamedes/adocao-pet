from django import forms
from adopet.models import Animal

class CreatePetForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nome', 'raca', 'porte', 'peso', 'tipo_animal', 'idade']