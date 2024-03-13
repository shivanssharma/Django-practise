
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def shivanshapp(request):
    return render(request,'login page.html')