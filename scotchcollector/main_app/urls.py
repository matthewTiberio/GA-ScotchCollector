from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('scotch/', views.scotch_index, name='index'),
    path('scotch/<int:scotch_id>/', views.scotch_detail, name='detail'),
]