from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world_view(request):
    return HttpResponse('<h1>Welcome To Django - The Rapid Web Application Dev Framework</h1>')
