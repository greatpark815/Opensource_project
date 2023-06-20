from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect
from . models import User
from django.http import HttpResponse
from main.views import main

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(username=username, password=password)
        if user is not None:
            print(username + "님 환영합니다")
            login(request,user)
            

        else:
            print("인증실패")
                
    return render(request,"sign/login.html")

def logout_view(request):
    logout(request)
    return redirect("sign:login")

def signup_view(request):
    if request.method == "POST":
        print(request.POST)
        username=request.POST["username"]
        password=request.POST["password"]
        firstname=request.POST["firstname"]
        lastname=request.POST["lastname"]
        email=request.POST["email"]
    
        
        user = User.objects.create_user(username,email,password)
        user.last_name= lastname
        user.first_name=firstname
        user.save()
        return redirect("sign:login")

    return render(request,"sign/signup.html")

def gotomain(request):
    return redirect('/main')