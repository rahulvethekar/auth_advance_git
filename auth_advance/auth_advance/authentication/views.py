from django.shortcuts import redirect, render

from .models import Register
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def RegistrationView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('uEmail')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if  Register.objects.filter(email = email).exists():
            messages.error(request,'Email id is already exist!')
            return redirect('cRegister')

        if not password1 == password2:
            messages.error(request,'password1 and password2 does not match')

        pwd = make_password(password2)

        obj = Register(name = name,email = email,username = username,password=pwd)
        obj.save()
        return redirect('cLogin')
    session_email = request.session.get('email')
    context = {'sessionEmail':session_email}
    template_name = 'authentication/register.html'
    return render(request,template_name,context)

        
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not Register.objects.filter(username = username).exists():
            messages.error(request,'Username does not exist')
            return redirect('cLogin')
        uname = Register.objects.get(username = username)
        pwd = uname.password
        check = check_password(password,pwd)
        if not check == False:
            request.session['username']=username
            return redirect('home')
        else:
            messages.error(request,'Wrong Credentials')
    template_name = 'authentication/login.html'
    return render(request,template_name)

def logoutView(request):

    request.session.clear()
    return redirect('cLogin')
    

def changePassword(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        opwd = request.POST.get('oldpwd')
        newpwd1 = request.POST.get('newpwd1')    
        newpwd2 = request.POST.get('newpwd2')

        if not Register.objects.filter(username=uname).exists():
            messages.error(request,'invalid username!')
            return redirect('changePassword')
        if newpwd1 != newpwd2:
            messages.error(request,'password1 and password2 does not match!')
            return redirect('changePassword')

        user = Register.objects.get(username=uname)
        encoded = user.password
        check = check_password(opwd,encoded)
        if check is not False:
            newpassword = make_password(newpwd1)
            user.password = newpassword
            user.save()
            return redirect('cLogin')

    template_name = 'change/form.html'
    return render (request,template_name)


def forgotPassword(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')

        if not Register.objects.filter(username = uname).exists():
            messages.error(request,'invalid username')
            return redirect('forgotPassword')

        if not Register.objects.filter(email = email).exists():
            messages.error(request,'invalid email id')
            return redirect('forgotPassword')

        subject = 'rest password'
        message = f'hey {uname}\nclick on the link to reset password\n http://127.0.0.1:8000/resetPassword/'
        
        send_mail(subject,
                    message,
                    'rahulvethekar95@gmail.com',
                    [email],
                    fail_silently=False

        )
        messages.success(request,'Email has been send successfully on your email id, please check it.')

    template_name = 'forgot/forgot.html'
    return render(request,template_name)


def forgotDetail(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd1 = request.POST.get('newpwd1')
        pwd2 = request.POST.get('newpwd2')

        if not Register.objects.filter(username=uname).exists():
            messages.error(request,'wrong username')
            return redirect('reset')

        if pwd1 != pwd2:
            messages.error(request,'password1 and password2 does not match!')
            return redirect('reset')

        newpassword = make_password(pwd2)
        user = Register.objects.get(username = uname)
        user.password = newpassword
        user.save()
        #messages.success(request,'password reset successfully!')
        return redirect('cLogin')

    template_name = 'forgot/forgotDetails.html'
    return render(request,template_name)

        

 






