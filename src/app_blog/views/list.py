from django.http import HttpRequest
from django.shortcuts import render
from app_blog.utility import query

def view(request: HttpRequest):
  if request.method == 'GET':
    posts = query('SELECT * FROM blog_post')
  return render(request, 'app_blog/list.html', {'posts': posts})
