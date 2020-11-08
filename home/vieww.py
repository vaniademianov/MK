from django.shortcuts import render
from main import models
from main.models import Ak
def home(request):
    what = Ak.objects.all()
    return render(request,r'C:\Users\User\Desktop\MK ONLINE DJANGO PROJECT\MK_ONLINE_FROM_VSS\main\templates\home\main.html',{'types': 'Offers', 'what':what})
def homeu(request):
    what = Ak.objects.all()
    return render(request,r'C:\Users\User\Desktop\MK ONLINE DJANGO PROJECT\MK_ONLINE_FROM_VSS\main\templates\home\ukraine.html',{'types': 'Offers', 'what':what})
# Create your views here.
