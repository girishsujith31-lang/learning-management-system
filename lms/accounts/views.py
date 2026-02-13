from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Profile

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another.')
            return render(request, 'accounts/register.html')

        user = User.objects.create_user(username=username, password=password)
        # Update the auto-created profile with the selected role
        profile = Profile.objects.get(user=user)
        profile.role = role
        profile.save()
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect('accounts:login')
    return render(request, 'accounts/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('core:dashboard')
        messages.error(request, 'Invalid username or password')
        
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')