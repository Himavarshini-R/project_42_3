# profile/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('achievements/', views.achievements, name='achievements'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
