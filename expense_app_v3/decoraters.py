from django.http import HttpResponse
from django.shortcuts import render , redirect

def userauthentic_register_login (view_func):
    def  wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func