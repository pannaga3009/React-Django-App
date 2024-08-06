from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET'])
def get_tasks(request):
    #Retreive all tasks from the database
    tasks = Task.objects.all()
    #Convert task objects to list of dict
   
    tasks_data = [{'id' : task.taskid, 'title': task.title, 'completed': task.completed} for task in tasks]
    return Response(tasks_data)

@csrf_exempt
@api_view(['POST'])
def add_tasks(request):
    #Get the task data from request
    title = request.data.get('title')
    completed = request.data.get('completed')
    taskid = request.data.get('taskid')

    #Create an new task object
    task = Task.objects.create(title=title, completed=completed)
    #Convert new task to a dictionary
    task_data = {'id': task.taskid, 'title': task.title, 'completed': task.completed}
    return Response(task_data)

@csrf_exempt
@api_view(['PUT'])
def update_task(request, pk):
    #Get the task to update
    task = Task.objects.get(taskid=pk)
    #Update the task fields with data from the request
    task.title = request.data.get('title', task.title)
    task.completed = request.data.get('completed', task.completed)
    task.save()
        
    task_data = {'id': task.taskid, 'title': task.title, 'completed': task.completed}
    print(task_data)
    return Response(task_data)

@csrf_exempt
@api_view(['DELETE'])
def delete_task(request, pk):
    task = Task.objects.get(taskid=pk)
    task.delete()
    return Response({'message': 'Task deleted successfully'})



