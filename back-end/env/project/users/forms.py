from django import forms

from django import forms

class SignInForm(forms.Form):
    username = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={'placeholder': 'Ime', 'class': 'validate'}))
    password = forms.CharField(max_length=50,
                                widget=forms.TextInput(attrs={'placeholder': 'Prezime', 'class': 'validate'}))