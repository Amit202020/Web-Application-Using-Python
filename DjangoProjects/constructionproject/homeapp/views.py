from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def  ban_home_view(request):
    return  HttpResponse('<html><body><h1>welcome to Ban  Home</h1><body></html>')
