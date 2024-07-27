from django.shortcuts import render,redirect
from .forms import RegisterForm, TaskForm
from .models import Task
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Your account creation has been successfull')
            user = form.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Something went wrong, try to register again')
    else:
        form = RegisterForm()
    
    context = {'form':form}
            
    return render(request,'register.html',context)

def login_page(request):
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        try:
            user = User.objects.get(username=Username)
        except:
            messages.error(request,"User doesn't exist")
        user = authenticate(username=Username,password=Password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or password doesn't match")
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('home')

@login_required(login_url="login")
def home_page(request):
    task_records = Task.objects.filter(user=request.user)
    context = {'task_records':task_records}
    
    return render(request,'home.html',context)

@login_required(login_url="login")
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    context = {'form':form}
    
    return render(request,'task_form.html',context)

@login_required(login_url="login")
def edit_task(request,id):
    task_to_edit = Task.objects.get(id=id)
    form = TaskForm(instance=task_to_edit)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task_to_edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    
    return render(request,'task_form.html',context)

@login_required(login_url="login")
def delete_task(request,id):
    task_to_delete = Task.objects.get(id=id)
    if request.method == 'POST':
        task_to_delete.delete()
        return redirect('home')
    context = {'task_to_delete':task_to_delete}
    return render(request,'delete_obj.html',context)