from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def teachers(request):
    return render(request, "teachers/teachers.html")

def courses(request):
    return render(request, "courses/courses.html")

def contact(request):
    form = ContactForm()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/contact.html", {
                "form": ContactForm(),
                "success": True
                })
            
    return render(request, "core/contact.html", {"form": form})
