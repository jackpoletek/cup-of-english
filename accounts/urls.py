from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    path("profile/", views.profile, name="profile"),
    path("admin/", views.admin_dashboard, name="admin_dashboard"),

    path(
        "activate/<uid64>/<token>/",
        views.activate_account,
        name="activate"
        ),

    path("resend-activation/", views.resend_activation, name="resend_activation"),
]
