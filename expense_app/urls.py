from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    #path('sub_cat/', views.sub_cat, name = 'sub_cat')
]