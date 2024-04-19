from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import WareForm

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def mycollection(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = WareForm(request.POST)

            if form.is_valid():
                form.save()
            else:
                form = WareForm()
            return render(request, 'MyCollection.html', {'form': form})
        else:
            form = WareForm()
            return render(request, 'mycollection.html', {'form': form})
    else:
        return redirect('http://127.0.0.1:8000/login/')

def othercollections(request):
    return render(request, 'othercollection.html')

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('http://127.0.0.1:8000/home/')
        else:
            messages.info(request, 'Login incorrect!')
            return redirect('http://127.0.0.1:8000/login/')
    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('http://127.0.0.1:8000/home/')

from .forms import RegisterForm

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/login/')
        else:
            if request:
                messages.info(request, 'You must define a username and your password must have at least 8 characters!')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



