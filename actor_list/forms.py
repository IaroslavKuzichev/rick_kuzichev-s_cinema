from django import forms
from .models import Actor


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        } 