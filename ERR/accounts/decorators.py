from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if(request.user.is_authenticated):
            return HttpResponseRedirect(reverse('homePage'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if(request.user.is_authenticated):
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('homePage'))
    
    return wrapper_func

def authenticate_all_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if(request.user == 'AnonymousUser'):
            return HttpResponseRedirect(reverse('homePage'))
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func