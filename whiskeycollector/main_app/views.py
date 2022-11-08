from django.shortcuts import render
from django.http import HttpResponse
from .models import Whiskey, WhiskeyTypes, TYPES

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def whiskey_index(request):
    whiskeys = Whiskey.objects.all()
    return render(request, 'main_app/index.html', { 'whiskeys': whiskeys })

def whiskey_detail(request, whiskey_id):
    whiskey = Whiskey.objects.get(id=whiskey_id)
    return render(request, 'main_app/detail.html', { 'whiskey': whiskey })
