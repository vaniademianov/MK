from django.shortcuts import render
from .models import Ak
def main(request):
    az = Ak.objects.all()
    return render(request,r'C:\Users\User\Desktop\MK ONLINE DJANGO PROJECT\MK_ONLINE_FROM_VSS\main\templates\main\main.html',{'types': 'Offers', 'az':az})
# Create your views here.
