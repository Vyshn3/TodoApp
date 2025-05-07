from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from todo.models import TODOO
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def signup(request):
    if request.method == 'POST':
        email_id = request.POST.get('email')
        pwd = request.POST.get('pwd')
        if User.objects.filter(username=email_id).exists():
            return render(request, 'signup.html', {'error': 'User with this email already exists.'})
        my_user = User.objects.create_user(username=email_id, password=pwd)
        my_user.save()
        return redirect('/login')

    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email_id = request.POST.get('email')
        pwd = request.POST.get('pwd')
        userr = authenticate(request, username=email_id, password=pwd)
        if userr is not None:
            auth_login(request, userr)
            return redirect('/todo')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password.'})

    return render(request, 'login.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/login') 


@login_required
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        obj = TODOO(title=title, user=request.user)
        obj.save()
        return redirect('/todo')  # Simply redirect to the todo page after saving
    res = TODOO.objects.filter(user=request.user, is_completed=False)
    completed_tasks = TODOO.objects.filter(user=request.user, is_completed=True, date__date=timezone.now().date())

    return render(request, 'todo.html', {'res': res, 'completed_tasks': completed_tasks})


def edit_todo(request, todo_id):
    todo_item = get_object_or_404(TODOO,srno=todo_id, user=request.user)

    if request.method == 'POST':
        new_title = request.POST.get('title')
        todo_item.title = new_title
        todo_item.save()
        return redirect('/todo')

    return render(request, 'edit_todo.html', {'todo': todo_item})


def delete_todo(request, todo_id):
    todo_item = get_object_or_404(TODOO,srno=todo_id, user=request.user)
    if request.method == 'POST':  # Optional: you could use GET too for delete
        todo_item.delete()
        return redirect('/todo')

    return render(request, 'confirm_delete.html', {'todo': todo_item})

def mark_complete(request, todo_id):
    # Fetch the todo item or return a 404 if it doesn't exist
    todo_item = get_object_or_404(TODOO, srno=todo_id, user=request.user)

    # Mark the task as completed and save the current date as the completion date
    todo_item.is_completed = True
    todo_item.date = timezone.now()
    todo_item.save()

    return redirect('/todo')
