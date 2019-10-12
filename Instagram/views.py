from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome home")

def about(request):
    return HttpResponse("This is out about page")
