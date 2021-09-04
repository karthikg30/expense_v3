from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),
    path('view_page', views.viewpage, name = 'view'),
    path('expense', views.expense_page, name = 'expense'),
    path('board', views.dashboard, name = 'board'),
    path('js', views.js, name = 'js'),
    path('load_data', views.load_data, name = 'load_data'),
    path('exp_load_data', views.exp_load_data, name = 'exp_load_data'),
    path('loginpage', views.loginpage, name = 'loginpage'),
    path('logout/', views.logoutpage, name = 'logout'),
    path('consolidate', views.consolidate, name = 'consolidate'),

    #path('delete/<int:pk>', views.editdate, name = 'delete'),
    #path('sub_cat/', views.sub_cat, name = 'sub_cat')
]