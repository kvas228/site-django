from .models import zakazi
from django.forms import ModelForm,TextInput,Textarea
from django import forms
from .models import articles

class zakaziForm(ModelForm):
    class Meta:
        model = zakazi
        fields = ['zazchik','zakaz']
        widgets = {
            "zazchik":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите название'}),
            "zakaz": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'}),
        }
class ImageForm(forms.ModelForm):
    class Meta:
        model = articles
        fields = ['title', 'image']