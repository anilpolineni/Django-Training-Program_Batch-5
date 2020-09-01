from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "index.html")


def welcome(request):
    return render(request, "welcome.html")


def about(request):
    return render(request, "about.html")
