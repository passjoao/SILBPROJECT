from .models import Request
from django import forms

class RequestSearchForm(forms.Form):
    search_text =  forms.CharField(
                    required = False,
                    label='Pesquisar:',
                    widget=forms.TextInput(attrs={'placeholder': 'digite aqui....'})
                  )