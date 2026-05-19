from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

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

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

handler404 = "core.views.error_404_view"
handler403 = "core.views.error_403_view"
handler500 = "core.views.error_500_view"
