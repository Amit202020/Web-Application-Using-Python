from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  btlc_partner_view(request):
    return  HttpResponse('<h1>Hello, world Partner</h1>')
