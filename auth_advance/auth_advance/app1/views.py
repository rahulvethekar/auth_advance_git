from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def HomeView(request):

    template_name = 'app1/home.html'
    return render(request,template_name)

def registrationForm(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')

    context = {'form':form}
    template_name = 'app1/registration.html'
    return render (request,template_name,context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password=password)
        if user is not None:
            login(request,user)
            print('login!!!!')
            return redirect('home')
        else:
            print('wrong passwrod!!!!1')
            messages.error(request,'wrong credentials!')

    template_name = 'app1/login.html'
    return render(request,template_name)

def Logout(request):
    logout(request)
    return redirect('logoutView')

def LogoutView(request):
    template_name = 'app1/logoutpage.html'
    return render(request,template_name)
