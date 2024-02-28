from django import forms
from .models import ToDo
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q

class RegisterationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        for fieldName in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldName].help_text = None 


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['ToDoNote']
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ToDoForm, self).__init__(*args, **kwargs)
        self.fields['ToDoNote'].label = 'ToDo'
    