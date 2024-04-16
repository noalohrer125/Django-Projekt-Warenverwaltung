from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def mycollection(request):
    return render(request, 'MyCollection.html')

def login(request):
    return render(request, 'login.html')

def regitster(request):
    return render(request, 'register.html')


def othercollections(request):
    return render(request, 'othercollection.html')
