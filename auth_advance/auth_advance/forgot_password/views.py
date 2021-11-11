from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import message, send_mail
from django.contrib.auth.hashers import make_password


# Create your views here.
def forgotPassword(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')

        if not User.objects.filter(username = uname).exists():
            messages.error(request,'invalid username')
            return redirect('forgotPassword')

        if not User.objects.filter(email = email).exists():
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

        if not User.objects.filter(username=uname).exists():
            messages.error(request,'wrong username')
            return redirect('reset')

        if pwd1 != pwd2:
            messages.error(request,'password1 and password2 does not match!')
            return redirect('reset')

        newpassword = make_password(pwd2)
        user = User.objects.get(username = uname)
        user.password = newpassword
        user.save()
        #messages.success(request,'password reset successfully!')
        return redirect('login')

    template_name = 'forgot/forgotDetails.html'
    return render(request,template_name)

        

 