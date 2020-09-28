from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  digital_iot_view(request):
    return  HttpResponse('<html><body><h1>welcome to IOT demo</h1><body></html>')

def  digital_UX_view(request):
    return  HttpResponse('<html><body><h1>welcome to UX demo</h1><body></html>')

def  digital_cloud_view(request):
    return  HttpResponse('<html><body><h1>welcome to CLOUD demo</h1><body></html>')
