from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def mycollection(request):
    if request.user.is_authenticated:
        return render(request, 'mycollection.html')
    else:
        return redirect('http://127.0.0.1:8000/login/')

def login(request):
    return render(request, 'login.html')

def regitster(request):
    return render(request, 'register.html')


def othercollections(request):
    return render(request, 'othercollection.html')
