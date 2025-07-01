from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignupForm,TodoForm
from django.contrib.auth.decorators import login_required
from .models import TodoList

def signup(request):
    form = SignupForm()
    
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)  
    return redirect('login')

@login_required  
def home(request):
    data = TodoList.objects.filter(user=request.user)
    return render(request, 'home.html',{'tasks':data})

@login_required
def add(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user 
            todo.save()
            return redirect('home') 
    else:
        form = TodoForm()
    return render(request,'addtodo.html', {'form': form})
        
@login_required
def delete_task(request, id):
    task =get_object_or_404(TodoList, id=id)
    task.delete()
    return redirect('home')

@login_required
def edit_task(request, id):
    task =get_object_or_404(TodoList, id=id)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm(instance=task)
    
    return render(request, 'edittodo.html', {'form': form})