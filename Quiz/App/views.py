from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from . import models


def sendEmail(request):
    content = render_to_string('mail.html', {'name': "Fawad", 'roll': 84, 'Class': "BsIT"})
    send_mail("PFSMS", "", "", ["fawadstar6@gmail.com"], html_message=content)
    messages.success(request, 'Email Send')


def stdLogin(request):
    # sendEmail(request)
    if request.method == "POST":
        Username = request.POST.get('Username')
        Pass = request.POST.get('Pass')
        user = authenticate(username=Username, password=Pass)
        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.warning(request, "Invalid Username OR Password")
            return redirect('Login')
    return render(request, 'login.html')


def stdLogout(request):
    logout(request)
    return redirect('Login')


@login_required(login_url='Login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='Login')
def quiz(request):
    user = models.User.objects.get(username=request.user)
    if models.Question.objects.filter(Coucre__Student=user):
        print("foooooonnd")
        data = models.Question.objects.filter(userAns="")
    else:
        messages.ERROR(request, "Sorry You Have Already Attempted Quiz")
    if request.method == "POST":
        for i in data:
            ans = request.POST.get(f'Ans{i.id}')
            print(ans)
            models.Question.objects.filter()
    return render(request, 'quiz.html', {'Qs': data})
