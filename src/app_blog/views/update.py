from django.http import HttpRequest
from django.shortcuts import redirect, render
from app_blog.utility import query

def view(request: HttpRequest, id: int):
  post = query('SELECT * FROM blog_post WHERE id = %s', [id])

  if not post:
    return render(request, 'app_blog/notfound.html', status=404)
  post = post[0]

  match request.method:
    case 'GET':
      return render(request, 'app_blog/update.html', {'post': post})
  
    case 'POST':
      title = request.POST.get('title')
      content = request.POST.get('content')

      newpost = query('UPDATE blog_post SET title=%s, content=%s WHERE id=%s', [title, content, id])

      return redirect(f'/blog/read/{id}')