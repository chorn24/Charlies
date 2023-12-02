from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest


# Create your views here.
def hub(request:HttpRequest):
    return render(request, "index.html")

def giga(request:HttpRequest):
    return render(request, "Giga.html")

def bltg(request:HttpRequest):
    return render(request, "brycelovesthisguy.html")

def about_us(request:HttpRequest):
    return render(request, "about_us.html")

def contacts(request:HttpRequest):
    return render(request, "contacts.html")

def location_hour(request:HttpRequest):
    return render(request, "location_hour.html")

def menu(request:HttpRequest):
    return render(request, "menu.html")