from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import WareForm

# Create your views here.
def home(request):
    return render(request, 'Home.html')

from django.shortcuts import render, redirect
from .models import Waren  # Stellen Sie sicher, dass Sie Ihr Modell entsprechend importieren
from .forms import WareForm  # Ihr Formular-Import

def add_product(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/login')  # Verwenden Sie den Namen der URL für die Umleitung

    form = WareForm(request.POST or None)  # Vereinfachte Formularinitialisierung
    if request.method == 'POST':
        if form.is_valid():
            ware = form.save(commit=False)
            ware.Eigentümer = request.user  # Stellen Sie sicher, dass der Benutzer als Eigentümer gesetzt ist, wenn das Modell ein `owner` Feld hat
            ware.save()
            # Nach dem Speichern, das Formular neu initialisieren oder Seite neu laden, um das neue Objekt zu sehen
            form = WareForm()

    ware = Waren.objects.filter(Eigentümer=request.user)  # Abrufen der Produkte, die dem Benutzer gehören
    print('error')
    return render(request, 'add.html', {'form': form})

def mycollection(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/login')  # Verwenden Sie den Namen der URL für die Umleitung

    form = WareForm(request.POST or None)  # Vereinfachte Formularinitialisierung
    if request.method == 'POST':
        if form.is_valid():
            ware = form.save(commit=False)
            ware.Eigentümer = request.user  # Stellen Sie sicher, dass der Benutzer als Eigentümer gesetzt ist, wenn das Modell ein `owner` Feld hat
            ware.save()
            # Nach dem Speichern, das Formular neu initialisieren oder Seite neu laden, um das neue Objekt zu sehen
            form = WareForm()

    ware = Waren.objects.filter(Eigentümer=request.user)  # Abrufen der Produkte, die dem Benutzer gehören
    print('error')
    return render(request, 'mycollection.html', {'form': form, 'waren': ware})

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
