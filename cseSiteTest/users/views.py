from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from .forms import CreateUserForm

import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
@login_required(login_url='login')
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def login_view(request):
    template = loader.get_template('login/loginWelcome.html')

    # u = User.objects.get(username='nishantbhat.cs21')
    # u.set_password('lolbhaikya')
    # u.save()

    return HttpResponse(template.render({}, request))

def register(request):
    template = loader.get_template('login/registerWelcome.html')
    return HttpResponse(template.render({}, request))

def registerStudent(request):
    if request.method == 'POST':
        # 'username': request.POST['email'].split("@")[0]
        # form = CreateUserForm({ **(request.POST), 'email': request.POST['email'],'username': "loluser" })
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("NOOOOOOO, there were some errors")
    else:
        form = CreateUserForm()
    context = { 'form': form }
    template = loader.get_template('login/registerStudent.html')
    return HttpResponse(template.render(context, request))

def registerFaculty(request):
    if request.method == 'POST':
        # 'username': request.POST['email'].split("@")[0]
        # form = CreateUserForm({ **(request.POST), 'email': request.POST['email'],'username': "loluser" })
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("NOOOOOOO, there were some errors")
    else:
        form = CreateUserForm()
    context = { 'form': form }
    template = loader.get_template('login/registerFaculty.html')
    return HttpResponse(template.render(context, request))

def loginStudent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Noooo, there were some errors")

    template = loader.get_template('login/loginStudent.html')
    return HttpResponse(template.render({}, request))

def logoutUser(request):
    logout(request)
    return redirect('login')

def loginFaculty(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Noooo, there were some errors")

    template = loader.get_template('login/loginFaculty.html')
    return HttpResponse(template.render({}, request))

# def displayStudent(request):
#     result = Student.objects.all().values()
#     print(len(result))
#     return HttpResponse("check the console, dude")

def reset_password(request):
    if request.method == 'POST':
        # email = request.POST.get('email')

        # print("YEHHhhhhhhhhhhhhhhhh")

        # port = 587  # For starttls
        # smtp_server = "smtp.gmail.com"
        # sender_email = "bokunishant28@gmail.com"
        # receiver_email = email
        # password = 'eurgyplbwpanhvmx'
        # message = "https://127.0.0.1:8000/reset_change_password/"

        # context = ssl.create_default_context()
        # with smtplib.SMTP(smtp_server, port) as server:
        #     server.ehlo()  # Can be omitted
        #     server.starttls(context=context)
        #     server.ehlo()  # Can be omitted
        #     server.login(sender_email, password)
        #     server.sendmail(sender_email, receiver_email, message)
        return redirect('password_reset_change')

    template = loader.get_template('login/reset_password.html')
    return HttpResponse(template.render({}, request))

def reset_change_password(request):
    if request.method == 'POST':
        u = User.objects.get(email=request.POST.get('email'))
        u.set_password(request.POST.get('password1'))
        u.save()
        return redirect('login')
    template = loader.get_template('login/reset_change_password.html')
    return HttpResponse(template.render({}, request))