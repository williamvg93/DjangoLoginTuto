from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

def tasks(request):
    return render(
        request, "layouts/tasks/tasks.html", {"pageTitle": "Tasks", "mainPageTitle": "Tasks"}
    )
