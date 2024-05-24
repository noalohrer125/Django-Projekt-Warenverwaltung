"""
URL configuration for warenverwaltung project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from collectionmanager.views import home
from collectionmanager.views import mycollection
from collectionmanager.views import login
from collectionmanager.views import othercollections
from collectionmanager.views import logout
from collectionmanager.views import sign_up
from collectionmanager.views import add_product
from django.conf import settings
from django.conf.urls.static import static
from collectionmanager.views import delete_product
from collectionmanager.views import add_category
from collectionmanager.views import send_e_mail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('mycollection/', mycollection),
    path('login/', login),
    path('othercollections/', othercollections),
    path('sign_up/', sign_up),
    path('logout/', logout),
    path('addproduct/', add_product),
    path('addcategory/', add_category),
    path('delete_product/<str:Name>/', delete_product, name='delete_product'),
    path('send-email/', send_e_mail, name='send_email'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
