from django.http import HttpRequest
from django.shortcuts import render, redirect
from app_todolist.utility import query

def view(request: HttpRequest):
  match request.method:
    case 'GET':
      return render(request, 'create.html')
    case 'POST':
      name = request.POST.get('name')
      query('INSERT INTO todo (name) VALUES (%s)', [name])
      return redirect('/todo/list/')
