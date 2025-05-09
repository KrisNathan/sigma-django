from django.http import HttpRequest
from django.shortcuts import render, redirect
from app_todolist.utility import query

def view(request: HttpRequest, id: int):
  todo = query('SELECT * FROM todo WHERE id=%s', [id])
  
  if not todo:
    return render(request, 'notfound.html', status=404)
  
  todo = todo[0]

  match request.method:
    case 'GET':
      return render(request, 'update.html', {'todo': todo})
    case 'POST':
      name = request.POST.get('name')
      newtodo = query('UPDATE todo SET name=%s WHERE id=%s', [name, id])
      return redirect('/todo/list/')
