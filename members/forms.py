from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import MembersModel

# create a form class

class LoginForm(AuthenticationForm):
    # add a custom field
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

# create a ModelForm
class MemberForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = MembersModel
        fields = ('name', 'surname', 'id_number', 'date_of_birth', 'baptized')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Surname', 'class': 'form-control'}),
            'id_number': forms.NumberInput(attrs={'placeholder': 'ID Number', 'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'Date of Birth', 'class': 'form-control'}),
            'baptized': forms.DateInput(attrs={'placeholder': 'Baptized', 'class': 'form-control'}),
        }
