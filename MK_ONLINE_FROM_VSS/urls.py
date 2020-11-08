"""MK_ONLINE_FROM_VSS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from main import views
from shop import view
from home import vieww
from home import vieww


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name=''),
    
    
    path('mkshop', view.shop, name=''),
    path('mkhome', vieww.home, name=''),
    path('mk_home_ukr', vieww.homeu, name=''),
]
