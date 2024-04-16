from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Home.html')

def mycollection(request):
    return render(request, 'MyCollection.html')