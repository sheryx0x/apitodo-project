from django.urls import path
from .views import todo_list, todo_create, todo_detail, todo_update, todo_delete

urlpatterns = [
    path('todos/', todo_list, name='todo-list'),
    path('todos/create/', todo_create, name='todo-create'),
    path('todos/<int:pk>/', todo_detail, name='todo-detail'),
    path('todos/<int:pk>/update/', todo_update, name='todo-update'),
    path('todos/<int:pk>/delete/', todo_delete, name='todo-delete'),
]
