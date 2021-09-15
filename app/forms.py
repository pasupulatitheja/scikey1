from django import forms
from .models import sci1
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Document

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'text',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type': 'password',
        'placeholder': 'Password'
    }))



class CreateUserForm(UserCreationForm):
    code = forms.IntegerField(label="code")
    groups = ('admin', 'admin'), ('manager', 'manager'), ('tl', 'Teamleader')
    # passw = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'type': 'password',
    #     'placeholder': 'Password'
    # }))

    catagary = forms.ChoiceField(choices=groups)
    class Meta:
        model = User


        # fields =  ['username','email','password1','password2']
        fields = ['username','code','email','catagary',]



class sci1data(forms.Form):
    class meta:
        model = sci1
        fields = '__all__'




class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )