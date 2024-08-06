from django.urls import path
from .views import get_tasks, add_tasks, update_task, delete_task

urlpatterns = [
    path('tasks/', get_tasks, name='get_tasks'),
    path('tasks/add/', add_tasks, name='add_tasks'),
    path('tasks/update/<int:pk>/', update_task, name='update_task'),
    path('tasks/delete/<int:pk>/', delete_task, name = 'delete_task'),
]