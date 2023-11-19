from django import forms
from . import models as mod
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterationForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
    def __init__(self, *args, **kargs):
        super(UserCreationForm, self).__init__(*args, **kargs)
        
        for fieldName in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldName].help_text = None 


class ToDoForm(forms.ModelForm):
    
    class Meta:
        model = mod.ToDo
        fields = ['ToDoNote']
    
    def __init__(self, *args, **kargs):
        super(ToDoForm, self).__init__(*args, **kargs)
        
        self.fields['ToDoNote'].label = 'ToDo'
    
        
        