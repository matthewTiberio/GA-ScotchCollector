from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Whiskey, WhiskeyTypes, TYPES

class WhiskeyCreate(CreateView):
    model = Whiskey
    fields = '__all__'

class WhiskeyUpdate(UpdateView):
    model = Whiskey
    fields = '__all__'

class WhiskeyDelete(DeleteView):
    model = Whiskey
    success_url = '/whiskey/'

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

def whiskey_create(request):
    types = TYPES
    return render(request, 'main_app/create.html', { 'types': types})

def whiskey_add(request):
    return HttpResponse(request.body)