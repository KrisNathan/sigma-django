from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def home(req: HttpRequest):
  return render(req, 'app_blog/index.html')