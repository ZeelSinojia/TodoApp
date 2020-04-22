from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addTodo, name='add'),
    path('complete/<todo_id>/', views.completeTodo, name='complete'),
    path('delete-completed/', views.deleteCompleted, name='delete-completed'),
    path('delete-all/', views.deleteAll, name='delete-all'),
]