from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import CategoryForm, WareForm
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Waren
from django.shortcuts import render, redirect
from .models import Waren  # Stellen Sie sicher, dass Sie Ihr Modell entsprechend importieren
from .forms import WareForm  # Ihr Formular-Import

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def add_category(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/login')
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('http://127.0.0.1:8000/mycollection')
        
    else:
        form = CategoryForm()
    
    return render(request, 'add_category.html', {'form': form})

def add_product(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/login')  # Verwenden Sie den Namen der URL für die Umleitung

    if request.method == 'POST':
        form = WareForm(request.POST, request.FILES)
        if form.is_valid():
            ware = form.save(commit=False)
            ware.Eigentümer = request.user
            ware.save()
            return redirect('http://127.0.0.1:8000/mycollection')  # Umleiten nach dem Speichern
        else:
            print('Productname is allready used. Please chose an other one!')
    else:
        form = WareForm()

    return render(request, 'add_product.html', {'form': form})

def mycollection(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/login')  # Verwenden Sie den Namen der URL für die Umleitung

    form = WareForm(request.POST or None)  # Vereinfachte Formularinitialisierung
    if request.method == 'POST':
        if form.is_valid():
            ware = form.save(commit=False)
            ware.save()
            # Nach dem Speichern, das Formular neu initialisieren oder Seite neu laden, um das neue Objekt zu sehen
            form = WareForm()

    ware = Waren.objects.filter(owner=request.user)  # Abrufen der Produkte, die dem Benutzer gehören
    return render(request, 'mycollection.html', {'form': form, 'waren': ware})

def othercollections(request):
    return render(request, 'othercollection.html')

def login(request):
    if request.method == 'POST':
        username = request.POST["username"] # Username aus Formular in Variable username speichern
        password = request.POST["password"] # Passwort aus Formular in Variable password speichern
        user = authenticate(request, username=username, password=password) # Ist der Username in der DB vorhanden? Ist das Passwort in der DB vohanden und gehört es zum eingegebenen User?
        # Wenn der User valide ist wird er angemeldet und auf die Home Seite umgeleitet
        if user is not None:
            auth_login(request, user)
            return redirect('http://127.0.0.1:8000/home/')
        # Wenn die Userinformationen inkorrekt sind erscheint eine Nachricht mit 'Login Incorrect' und der User wird auf die Login Seite umgeleitet
        else:
            messages.info(request, 'Login incorrect!')
            return redirect('http://127.0.0.1:8000/login/')
    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request) # User wird ausgeloggt
    return redirect('http://127.0.0.1:8000/home/') # User wird auf Home Seite umgeleitet

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/login/')
        else:
            if request:
                messages.info(request, 'You must define a unique username and your password must contain at least 8 characters!')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def delete_product(request, Name):
    if request.method == 'POST':
        # Verwende get_object_or_404 für bessere Fehlerbehandlung
        element = get_object_or_404(Waren, name=Name)
        element.delete()
        return HttpResponseRedirect('http://127.0.0.1:8000/mycollection/')
    else:
        return redirect('http://127.0.0.1:8000/mycollection/')
