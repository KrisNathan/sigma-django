from django.http import HttpRequest
from django.shortcuts import redirect
from app_todolist.utility import query

def view(request: HttpRequest, id: str):
  if request.method == 'GET':
    todo = query('SELECT id FROM todo WHERE id=%s', [id])
    if todo:
      result = query('DELETE FROM todo WHERE id=%s', [id])
  return redirect('/todo/list/')