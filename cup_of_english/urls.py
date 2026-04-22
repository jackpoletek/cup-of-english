from django.contrib import admin
from django.urls import path, include

from courses import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Core pages
    path("", include("core.urls")),

    # Accounts
    path("", include("accounts.urls")),

    # Courses
    path("courses/", include("courses.urls")),

    # Enrollments
    path("enrollments/", include("enrollments.urls")),

    # Teachers
    path("teachers/", include("teachers.urls")),

    # Payments
    path("payments/", include("payments.urls")),
]

handler404 = "core.views.error_404_view"
handler403 = "core.views.error_403_view"
handler500 = "core.views.error_500_view"
