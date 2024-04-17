from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def mycollection(request):
    if request.user.is_authenticated:
        return render(request, 'mycollection.html')
    else:
        return redirect('http://127.0.0.1:8000/login/')

# def login(request):
#     return render(request, 'login.html')




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
            return redirect('http://127.0.0.1:8000/login/')
    else:
        return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('http://127.0.0.1:8000/home/')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'register.html', context)
