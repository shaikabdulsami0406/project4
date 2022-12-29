from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def shaik(request):
    return HttpResponse('<marquee>hello SHAIK</marquee>')
def sami(request):
    return HttpResponse('<h1> hi sami</h1>')