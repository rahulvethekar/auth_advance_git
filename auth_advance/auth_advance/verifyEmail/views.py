from django.shortcuts import redirect, render
import random
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.

def emailVerification(request):
    if request.method == 'POST':
        email = request.POST.get('uEmail')
        otp = random.randint(1000,9999)
        request.session['otp'] = otp
        request.session['email'] = email
        subject = 'Verify your Email'
        message = f'Email Verification OTP:-{otp}'
        send_mail(
                subject,
                message,
                'rahulvethekar95@gmail.com',
                [email],
                fail_silently=False
        )
        return redirect('otpVerify')
    template_name = 'verifyEmail/verifyEmail.html'
    return render(request,template_name)

def otpVerify(request):
    if request.method == 'POST':
        otp = request.POST.get('uOTP')
        sessionOTP = request.session.get('otp')
        print(sessionOTP)
        print(otp)
        if int(otp) == int(sessionOTP):
            return redirect('cRegister')
        else:
            messages.error(request,'Invalid OTP Please Enter Valid OTP!')
    template_name = 'verifyEmail/otpVerify.html'
    return render(request,template_name)

