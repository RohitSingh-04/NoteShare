from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Notes
from .methods import Opened_Note

# Create your views here.
def home(request):
    return render(request=request, template_name="home.html", context = { "page_title" : "home - New", "new": True})

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Add logic to save user to the database

        if User.objects.filter(username = username).exists():
            return render(request, 'register.html', {'page_title': 'Register - Error', 'message': 'Username already exists!', 'message_type': 'error'})
        
        if User.objects.filter(email = email).exists():
            return render(request, 'register.html', {'page_title': 'Register - Error', 'message': 'Email already exists!', 'message_type': 'error'})

        user = User.objects.create_user(username=username, password=password, email=email)  
        if not user:
            return render(request, 'register.html', {'page_title': 'Register - Error', 'message': 'User creation failed!', 'message_type': 'error'})
        else:
            user.save()
            return render(request, 'home.html', {'message': 'User created successfully!', 'message_type': 'success'})
    if request.method == "GET":
        return render(request=request, template_name="register.html", context = { "page_title" : "Register"})
    
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Add logic to authenticate user

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request=request, template_name="home.html", context = { "page_title" : "home"})
        else:
            return render(request, 'login.html', {'page_title': 'Login - Error', 'message': 'Invalid credentials!', 'message_type': 'error'})
    if request.method == "GET":
        return render(request=request, template_name="login.html", context = { "page_title" : "Login"})
    
@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def save_note(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        note = Notes(title=title, content=content, author=request.user)
        note.save()
        url = reverse('open_note', args=[note.id])
        return redirect(f'{url}?message=Note saved successfully!&message_type=success')

@login_required(login_url='/login/')
def profile(request):
    return render(request=request, template_name="profile.html", context = {"page_title" : "Profile"})

@login_required(login_url='/login/')
def share_note(request, note_id):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        note = Notes.objects.get(id=note_id)
        
        user_to_share = User.objects.get(username=user_name)

        if request.user != note.author:
            
            url = reverse('open_note', args=[note.id])
            return redirect(f'{url}?message=You do not have permission to share this note!&message_type=warning')

        if note and user_to_share:
            note.shared_with.add(user_to_share)
            note.save()
            url = reverse('open_note', args=[note.id])
            return redirect(f'{url}?message=Note shared successfully!&message_type=success')
        else:
            url = reverse('open_note', args=[note.id])
            return redirect(f'{url}?message=Note not found!&message_type=error')

@login_required(login_url='/login/')
def open_note(request, note_id):
    note = Notes.objects.get(id=note_id)
    message = request.GET.get('message', None)
    message_type = request.GET.get('message_type', None)

    if note:
        if note.author == request.user or request.user in note.shared_with.all():
            if message:
                return render(request, 'home.html', {'message': message, 'message_type': message_type}|Opened_Note(note))
            else:
                return render(request, 'home.html', Opened_Note(note))
        else:
            return render(request, 'home.html', {'message': 'You do not have permission to view this note!', 'message_type': 'warning'})
    else:
        return render(request, 'home.html', {'message': 'Note not found!', 'message_type': 'error'})

@login_required(login_url='/login/')
def delete_note(request, note_id):
    ...

@login_required(login_url='/login/')
def show_notes(request):
    user_notes = Notes.objects.filter(author = request.user)
    shared_notes = Notes.objects.filter(shared_with = request.user)

    return render(request=request, template_name="home.html", context = { "page_title" : "Show Notes", "user_notes": user_notes, "shared_notes": shared_notes, "show_notes": True})

@login_required(login_url='/login/')
def update_note(request, note_id):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')

        note = Notes.objects.get(id=note_id)

        if not note:
            return redirect('new', message='Note not found!', message_type='error')

        if note.author != request.user:
            url = reverse('open_note', args=[note.id])
            return redirect(f'{url}?message=You do not have permission to update this note!&message_type=warning')

        note.title = title
        note.content = content
        note.save()
        url = reverse('open_note', args=[note.id])
        return redirect(f'{url}?message=Note updated successfully!&message_type=success')
    