from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoItem

def index(request):
    items = TodoItem.objects.all()
    context = {"todos": items}
    return render(request, 'todos/index.html', context)

def add(request):
    if request.method == 'POST':
        item = TodoItem(text=request.POST['item'])
        item.save()
        return redirect("todos:index")
    else:
        return render(request, "todos/index.html")

def doing(request):
    if request.method == 'POST':
        item = TodoItem.objects.get(pk=request.POST['doing_id'])
        item.doing = True
        item.done = False
        item.save()
        return redirect('todos:index')
    else:
        return render(request, "todos/index.html")


def done(request):
    if request.method == 'POST':
        item = TodoItem.objects.get(pk=request.POST['id'])
        item.done = True
        item.doing = False
        item.save()
        return redirect("todos:index")
    else:
        return render(request, "todos/index.html")

def delete(request):
    if request.method == 'POST':
        item = TodoItem.objects.get(pk=request.POST['delete_id'])
        item.delete()
        return redirect("todos:index")
    else:
        return render(request, "todos/index.html")