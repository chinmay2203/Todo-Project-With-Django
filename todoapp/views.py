from django.shortcuts import render,redirect,get_object_or_404
from . forms import Registerform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task

# Create your views here.

@login_required
def home(request):
        tasks = Task.objects.filter(user=request.user)
        return render(request, "index.html", {'tasks': tasks})
    


def register_view(request):
    
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Registration completed successfully! Please login.")

            return redirect('todoapp:login')

    else:
        form = Registerform()

    return render(request, "register.html", {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('todoapp:home')

        else:
            return render(request, "login.html")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('todoapp:login')


def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('todoapp:home')



@login_required
def add_task(request):
    if request.method == "POST":
        Task.objects.create(
            user=request.user,
            title=request.POST['title'],
            description=request.POST['description'],
            due_date=request.POST['due_date']
        )
    return redirect('todoapp:home')


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST['due_date']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('todoapp:home')


    return render(request, "edit_task.html", {'task': task})