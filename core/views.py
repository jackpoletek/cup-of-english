from django.shortcuts import redirect, render
from .forms import ContactForm

from django.core.mail import send_mail
from django.conf import settings

from django.contrib import messages
from courses.models import Course


def index(request):
    featured_courses = (
        Course.objects.filter(is_active=True)
        .order_by("course_type", "level")[:6]
    )

    return render(
        request,
        "core/index.html",
        {
            "featured_courses": featured_courses,
        }
    )


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

            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # Send confirmation email
            send_mail(
                subject=f"New Contact Message from {name}",
                message=f"Message from {name}. ({email}):\n\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")

            return redirect("core:contact")

        else:
            form = ContactForm()

    return render(request, "core/contact.html", {"form": form})


def error_404_view(request, exception=None):
    return render(request, "404.html", status=404)


def error_403_view(request, exception=None):
    return render(request, "403.html", status=403)


def error_500_view(request, exception=None):
    return render(request, "500.html", status=500)
