from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Username not exists")
            return redirect('')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Password invalid")
            return redirect('')
        
        else:
            login(request, user)
            return redirect('/upload')
    return render(request, 'login_page.html')


@login_required(login_url="")
def lgout(request):
    logout(request)
    return redirect("/")


def sign_up_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gmail = request.POST.get('gmail')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/sign')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = gmail,
            username = username
        )

        user.set_password(password)
        user.save()

    return render(request, 'signup_page.html')

@login_required(login_url='')
def upload_page(request):
    if request.method == "POST":
        notes = request.POST.get('notes')
        Imag = request.FILES.get('Imag')
        docment = request.FILES.get('docment')

        user = request.user

        uplod.objects.create(
            notes = notes,
            Imag = Imag,
            docment = docment,
            user = user
        )



        return redirect('/upload')

    return render(request, 'upload_page.html')

