from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_tasks( request ):
	tasks = Task.objects.all()
	# print(tasks)
	return render( request, 'list_tasks.html', { "tasks": tasks })

def create_task( request ):
	task = Task(title = request.POST['title'], description = request.POST['description'])
	task.save()
	return redirect('/')

def delete_task(request, task_id):
	taskToDelete = Task.objects.get(id=task_id)
	taskToDelete.delete()
	return redirect('/')