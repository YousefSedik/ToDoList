from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from .forms import ToDoForm, RegisterationForm
from django.contrib.auth.forms import AuthenticationForm 
from . import models

# Create your views here.


def login_page(re):
    context = {}
    if re.method == 'POST':
        form = AuthenticationForm(re, data=re.POST)
        if form.is_valid():
            user = form.get_user() 
            login(re, user) 
            return redirect('/')
        else:
            context['message'] = ['wrong password or username!']
    return render(re, 'registration/login.html', context)

def sign_up(request):
    if request.user.is_authenticated:
        logout(request) 
    if request.method == 'POST':
        form = RegisterationForm(request.POST or None )
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
        
    else:
        form = RegisterationForm()
        
    return render(request, 'registration/sign-up.html', {'form':form})

def log_out(re):
    if re.user.is_authenticated:
        logout(re)
    return redirect('/home')




@login_required(login_url='/login')
def home(request):
       
    form = ToDoForm()
    all_todos = models.ToDo.objects.filter(user=request.user)
    
    return render(request, 'main/home.html', context={'all_todos':all_todos, 'form':form})

@login_required(login_url='/login')
def add(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST or None, user=request.user)
        if form.is_valid():
            todo_to_context = form.save(commit=False)
            todo_to_context.user = request.user
            todo_to_context.save()
            return render(request, 'main/todoelement.html', context={'todo':todo_to_context})
    return HttpResponse('')


@login_required(login_url='/login')
def delete_todo(request, pk=None):
    ToDo = models.ToDo.objects.filter(id=pk).first()
    if request.user == ToDo.user:
        ToDo.delete()
    
    return HttpResponse('')
        
        
@login_required(login_url='/login')
def check_uncheck(request, pk):
    ToDo = models.ToDo.objects.filter(id=pk).first()
    if request.user == ToDo.user:
        ToDo.is_done = not ToDo.is_done
        ToDo.save()
    todo = models.ToDo.objects.filter(id=pk).first()
    return render(request, 'main/todoelement.html', {'todo':todo})
    
    



