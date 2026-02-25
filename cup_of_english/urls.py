from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Core pages
    path("", include("core.urls")),

    # Accounts
    path("accounts/", include("accounts.urls")),

    # Courses
    path("courses/", include("courses.urls")),

    # Teachers
    path("teachers/", include("teachers.urls")),

    # Payments
    path("payments/", include("payments.urls")),
]
