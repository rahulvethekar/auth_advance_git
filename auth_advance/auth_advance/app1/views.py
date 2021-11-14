from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .middleware import articleMiddleware

# Create your views here.
def HomeView(request):

    template_name = 'app1/home.html'
    return render(request,template_name)

@articleMiddleware
def articleView(request):
    template_name = 'app1/article.html'
    return render(request,template_name)

