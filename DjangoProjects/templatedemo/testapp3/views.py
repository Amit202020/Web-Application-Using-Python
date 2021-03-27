from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def template_view(request):
    #pp='<h1> Welcome To Template </h1>'
    #return HttpResponse(pp)
    return render(request,'testapp3/results.html')
