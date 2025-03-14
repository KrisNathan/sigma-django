from django.shortcuts import render, HttpResponse
from django.http import HttpRequest

# Create your views here.
# def index(request: HttpRequest):
#   return HttpResponse("Hello world!")

def view(request: HttpRequest):
  return render(request, 'app_landing/index.html')
