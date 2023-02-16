from .models import HomeModel
from django import forms
from django.forms import ModelForm

class ReservationsForm(forms.ModelForm):
    class Meta:
        model = HomeModel
        fields = ('title','text')
        