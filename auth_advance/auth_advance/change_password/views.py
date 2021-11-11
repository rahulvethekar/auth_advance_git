from django.shortcuts import redirect, render
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def changePassword(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        opwd = request.POST.get('oldpwd')
        newpwd1 = request.POST.get('newpwd1')    
        newpwd2 = request.POST.get('newpwd2')

        if not User.objects.filter(username=uname).exists():
            messages.error(request,'invalid username!')
            return redirect('changePassword')
        if newpwd1 != newpwd2:
            messages.error(request,'password1 and password2 does not match!')
            return redirect('changePassword')

        user = User.objects.get(username=uname)
        encoded = user.password
        check = check_password(opwd,encoded)
        if check is not False:
            newpassword = make_password(newpwd1)
            user.password = newpassword
            user.save()
            return redirect('login')

    template_name = 'change/form.html'
    return render (request,template_name)



