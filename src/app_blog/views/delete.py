from django.http import HttpRequest
from django.shortcuts import redirect
from app_blog.utility import query

def view(request: HttpRequest, id: int):
  if request.method == 'GET':
    post = query('SELECT id FROM blog_post WHERE id = %s', [id])
    if post:
      result = query('DELETE FROM blog_post WHERE id = %s', [id])
      print(result)
  
  return redirect('/blog/list/', name="blog_list")
