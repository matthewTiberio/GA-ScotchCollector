from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.http import HttpResponse
from .models import Whiskey, WhiskeyTypes, TYPES
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = 'whiskeycollectorapp'

class WhiskeyDelete(LoginRequiredMixin, DeleteView):
    model = Whiskey
    success_url = '/whiskey/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def whiskey_index(request):
    whiskeys = Whiskey.objects.all()
    types = WhiskeyTypes.objects.all()
    return render(request, 'main_app/index.html', { 'whiskeys': whiskeys, 'types': types })

@login_required
def whiskey_detail(request, whiskey_id):
    whiskey = Whiskey.objects.get(id=whiskey_id)
    type = WhiskeyTypes.objects.get(id=whiskey.type_id)
    return render(request, 'main_app/detail.html', { 'whiskey': whiskey, 'type': type })

@login_required
def whiskey_create(request):
    types = TYPES
    return render(request, 'main_app/create.html', { 'types': types})

@login_required
def whiskey_add(request):
    data = request.POST
    name = data["name"]
    whiskeyType = WhiskeyTypes.objects.get(type=data["type"])
    type_id = whiskeyType.id
    origin = data["origin"]
    subType = data["subType"]
    price = data["price"]
    volume = data["volume"]
    description = data["description"]
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            image_url = f"{S3_BASE_URL}{BUCKET}/{key}"
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    w = Whiskey(name=name, type_id=type_id, origin=origin, subType=subType, price=price, volume=volume, description=description, user=request.user, image_url=image_url)
    w.save()
    return redirect('index')

@login_required
def whiskey_edit(request, whiskey_id):
    whiskey = Whiskey.objects.get(id=whiskey_id)
    types = TYPES
    currentType = WhiskeyTypes.objects.get(id=whiskey.type_id)
    return render(request, 'main_app/edit.html', { 'whiskey': whiskey, 'currentType': currentType, 'types': types })

@login_required
def whiskey_update(request, whiskey_id):
    whiskey = Whiskey.objects.get(id=whiskey_id)
    data = request.POST
    name = data['name']
    whiskeyType = WhiskeyTypes.objects.get(type=data["type"])
    type_id = whiskeyType.id
    origin = data["origin"]
    subType = data["subType"]
    price = data["price"]
    volume = data["volume"]
    description = data["description"]
    w = Whiskey(id=whiskey_id, name=name, type_id=type_id, origin=origin, subType=subType, price=price, volume=volume, description=description)
    w.save()
    return redirect('index')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)