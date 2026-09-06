from django import forms
from .models import Movie, Character

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'