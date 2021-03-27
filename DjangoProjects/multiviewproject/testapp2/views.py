from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def account_view(request):
    return HttpResponse('<h1>Welcome To Account</h1>')
def order_view(request):
    return HttpResponse('<h1>Welcome To Order</h1>')
def hr_view(request):
    return HttpResponse('<h1>Welcome To Hr</h1>')
def product_view(request):
    return HttpResponse('<h1>Welcome To Product</h1>')
