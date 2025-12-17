# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# List To-Dos
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/list.html', {'todos': todos})

# Add To-Do
def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo/form.html', {'form': form})

# Edit To-Do
def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('todo_list')
    return render(request, 'todo/form.html', {'form': form})

# Delete To-Do
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')
