from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('whiskey/', views.whiskey_index, name='index'),
    path('whiskey/<int:whiskey_id>/', views.whiskey_detail, name='detail'),
    path('whiskey/create/', views.whiskey_create, name="whiskey_create"),
    path('whiskey/add/', views.whiskey_add, name="whiskey_add"),
    path('whiskey/<int:pk>/update/', views.WhiskeyUpdate.as_view(), name='whiskey_update'),
    path('whiskey/<int:pk>/delete/', views.WhiskeyDelete.as_view(), name='whiskey_delete'),
]