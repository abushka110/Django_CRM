from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "Username or Password is incorrect! Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

# TODO: separate login page
# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect('home')

def register_user(request):
    logout(request)
    return render(request, 'register.html', {})