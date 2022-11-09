from django.contrib import admin
from .models import Whiskey, WhiskeyTypes

# Register your models here.
admin.site.register(Whiskey)
admin.site.register(WhiskeyTypes)