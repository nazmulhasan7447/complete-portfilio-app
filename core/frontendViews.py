from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

def index(request):


    return render(request, 'frontend/index.html')


def project(request):


    return render(request, 'frontend/project.html')