from django.http import HttpRequest
from django.shortcuts import render
from app_todolist.utility import query

def view(request: HttpRequest):
  if request.method == 'GET':
    todos = query('SELECT * FROM todo')
    return render(request, 'list.html', {'todos': todos})
