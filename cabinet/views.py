from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import loader
from .models import Profile


def profile_view(request):
    profile = Profile.objects.filter(user = request.user)
    data = {'profile': profile.values(), 'username': request.user.username }
    return render(request, 'profile/index.html', context = data)
    
# def logout_view(request):
    # logout(request)
    # return redirect(login) 