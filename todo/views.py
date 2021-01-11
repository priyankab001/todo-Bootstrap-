from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks,'form':form}
    return render(request=request, template_name='tasks/list.html', context=context)

def update_task(request,primary_key):
    task = Task.objects.get(id=primary_key)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {"form":form}
    return render(request=request,template_name='tasks/update_task.html',context=context)

def delete_task(request,pk):
    """"""
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    context = {'item':task}
    return render(request=request,template_name='tasks/delete.html',context=context)