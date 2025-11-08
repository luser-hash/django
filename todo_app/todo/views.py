from django.shortcuts import redirect, render, get_object_or_404
from .models import ToDo
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils import timezone

user = get_user_model

# Create your views here.


def home(request):
    todos = ToDo.objects.all()
    total = todos.count()
    done = todos.filter(is_done=True).count()
    return render(request, 'home.html', {
        'todo': todos,
        'total': total,
        'done': done,
        })


def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        is_done = request.POST.get('is_done') == 'on'
        due_at_raw = request.POST.get('due_at')

        due_at = None
        if due_at_raw.strip():
            naive = datetime.fromisoformat(due_at_raw)
            due_at = timezone.make_aware(naive)

        if title:
            ToDo.objects.create(
                owner=request.user,
                title=title,
                description=description,
                is_done=is_done,
                due_at=due_at
            )
            return redirect('home')
    return render(request, 'form.html')


def update_todo(request, pk):
    try:
        todo = ToDo.objects.get(pk=pk, owner=request.user)
    except ToDo.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        is_done = request.POST.get('is_done') == 'on'
        due_at = request.POST.get('due_at')

        if title:
            todo.title = title

        if description is not None and description.strip() != '':
            todo.description = description

        todo.is_done = is_done
        if due_at.strip():
            naive = datetime.fromisoformat(due_at)
            todo.due_at = timezone.make_aware(naive)
        todo.save()
        return redirect('home')
    return render(request, 'update.html', {'todo': todo})


def toggle_done(request, pk):
    todo = get_object_or_404(ToDo, pk=pk, owner=request.user)
    todo.is_done = not todo.is_done
    todo.save()
    return redirect('home')


def delete_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk, owner=request.user)
    todo.delete()
    return redirect('home')