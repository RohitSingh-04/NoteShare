from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request=request, template_name="home.html", context = { "page_title" : "home"})

def save_note(request):
    ...

def share_note(request):
    ...