from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.hashers import make_password
import random


# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('market:home')


def forget(request):
    if request.method == "POST":
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.info(request, "Enter New Password.")
            return render(request, 'update.html', {"username": email})
        else:
            messages.info(request, "User not found")
            return redirect('accounts:forget')
    return render(request, "forget.html")


def update(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['conf_pass']
        key = ['@', "&", "$", "*"]
        if any(i in password for i in key):
            if(len(password) > 6):
                if(password == password2):
                    password = make_password(password)
                    User.objects.filter(email=email).update(
                        password=password)
                    messages.info(request, "Password Updated Successfully!")
                    return redirect('accounts:login')
                else:
                    messages.info(request, "Passord Doesn't Match!")
                    return render(request, 'update.html', {"username": email})
            else:
                messages.info(
                    request, 'Password must be greater than 6 characters!')
                return render(request, 'update.html', {"username": email})
        else:
            messages.info(
                request, 'Password must contain atleast one of the following special characters! (@, $, &, *)')
            return render(request, 'update.html', {"username": email})
    else:
        return render(request, "update.html")


def login(request):
    cap_val = random.randrange(1000, 100000)
    str_num = str(cap_val)

    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        captcha = request.POST.get('captcha')
        cap = request.POST.get('value')
        print(cap)
        print(captcha)
        if str(captcha) == cap:

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('/')
            else:
                messages.info(request, 'invalid username or password')
                return redirect('accounts:login')
        else:
            messages.info(request, 'invalid captcha')
            return redirect('accounts:login')

    return render(request, 'login.html', {'img': str_num})


def signup(request):
    if request.method == "POST":
        username = request.POST['org_name']
        email = request.POST['org_email']
        password = request.POST['password']
        password2 = request.POST['conf_pass']

        key = ['@', "&", "$", "*"]
        if any(i in password for i in key):
            if(len(password) > 6):
                if(password == password2):
                    if User.objects.filter(username=username).exists():
                        messages.info(request, "User Already Exist!")
                        return redirect("accounts:signup")
                    elif User.objects.filter(email=email).exists():
                        messages.info(request, "Email Already Exist!")
                        return redirect("accounts:signup")
                    else:
                        user = User.objects.create_user(
                            username=username, email=email, password=password)
                        user.save()
                        messages.info(request, 'Account Created Successfully!')
                        return redirect("accounts:login")
                else:
                    messages.info(request, "Passord Doesn't Match!")
                    return redirect("accounts:signup")
            else:
                messages.info(
                    request, 'Password must be greater than 6 characters!')
                return redirect("accounts:signup")
        else:
            messages.info(
                request, 'Password must contain atleast one of the following special characters! (@, $, &, *)')
            return redirect("accounts:signup")
    else:
        return render(request, 'signup.html')
