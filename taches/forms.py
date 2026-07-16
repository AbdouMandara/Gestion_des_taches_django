from django import forms
from .models import Projet

class ProjetForm(forms.ModelForm) :
    class Meta :
        model = Projet
        fields = ['nom', 'description_projet']

        labels = {
            'nom' : 'Nom du projet',
            'description_projet' : 'Description du projet'
        }

        widgets = {
            'nom' : forms.TextInput(attrs={
                'class' : 'input input-bordered w-full',
                'placeholder' : 'Entrez le nom du projet'
            }),
            'description_projet' : forms.Textarea(attrs={
                'class' : 'textarea textarea-bordered w-full',
                'placeholder' : 'Entrez la description du projet',
                'rows' : 4
            })
        }