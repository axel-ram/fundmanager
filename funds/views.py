from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>hello</h1>')

def fundList(request):
    return HttpResponse('<h1>fund list</h1>')

