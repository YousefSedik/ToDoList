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
    
    
    def clean(self):
        to_clean = super().clean()
        is_exist = ToDo.objects.filter(Q(ToDoNote=to_clean.get('ToDoNote')) & Q(user=self.user) )
        if len(to_clean.get('ToDoNote')) < 5:
            self.add_error('ToDoNote', 'TODO Should be more than 4 charcaters! ')
        if is_exist:
            self.add_error('ToDoNote', 'TODO Already Exists! ')
            
        return to_clean 
        
