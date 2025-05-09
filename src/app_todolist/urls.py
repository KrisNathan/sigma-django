from django.urls import path
from app_todolist.views import create, list, delete, update

urlpatterns = [
    path('create/', create.view, name='todo_create'),
    path('list/', list.view, name='todo_list'),
    path('delete/<uuid:id>/', delete.view, name='todo_delete'),
    path('update/<uuid:id>/', update.view, name='todo_update'),
]