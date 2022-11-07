from django.shortcuts import render
from django.http import HttpResponse
from .models import Scotch

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def scotch_index(request):
    scotchs = Scotch.objects.all()
    return render(request, 'scotch/index.html', { 'scotchs': scotchs })

def scotch_detail(request, scotch_id):
    scotch = Scotch.objects.get(id=scotch_id)
    return render(request, 'scotch/detail.html', { 'scotch': scotch })
