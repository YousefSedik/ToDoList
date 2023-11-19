from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required 
from .forms import ToDoForm, RegisterationForm
from . import models
# Create your views here.
@login_required(login_url='/login')
def home(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
        return redirect('home')

    else:    
        form = ToDoForm()
        try:
            all_todos = models.ToDo.objects.filter(user=request.user)
        except:
            all_todos = None
        print(all_todos)
        return render(request, 'main/home.html', context={'all_todos':all_todos, 'form':form})


@login_required(login_url='/login')
def delete_todo(request, pk=None):
    
    ToDo = models.ToDo.objects.filter(id=pk).first()
    if request.user == ToDo.user:
        ToDo.delete()
    
    return redirect('/home')
        
        
@login_required(login_url='/login')
def check_uncheck(request, pk):
    
    ToDo = models.ToDo.objects.filter(id=pk).first()
    if request.user == ToDo.user:
        if ToDo.is_done:
            ToDo.is_done = False
        else:
            ToDo.is_done = True
        ToDo.save()
    
    return redirect('/home')
    
    

def sign_up(request):
    if request.user.is_authenticated:
        logout(request) 
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
        
    else:
        form = RegisterationForm()
        
    return render(request, 'registration/sign-up.html', {'form':form})


