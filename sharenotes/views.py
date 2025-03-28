from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Notes

# Create your views here.
def home(request):
    return render(request=request, template_name="home.html", context = { "page_title" : "home"})

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

        return render(request, 'home.html', {'message': 'Note saved successfully!', 'message_type': 'success'})
    
    if request.method == "GET":
        return render(request=request, template_name="save_note.html", context = { "page_title" : "Save Note"})

@login_required(login_url='/login/')
def share_note(request):
    ...

@login_required(login_url='/login/')
def open_note(request, note_id):
    ...

@login_required(login_url='/login/')
def delete_note(request, note_id):
    ...

@login_required(login_url='/login/')
def open_shared_notes(request):
    ...