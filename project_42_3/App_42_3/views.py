# profile/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def achievements(request):
    return render(request, 'achievements.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')
