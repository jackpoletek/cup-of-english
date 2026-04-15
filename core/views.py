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

def error_404_view(request, exception):
    return render(request, "404.html", status=404)

def error_403_view(request, exception):
    return render(request, "403.html", status=403)

def error_500_view(request):
    return render(request, "500.html", status=500)
