from django.urls import path
from . import views

app_name = "payments"

urlpatterns = [
    path("checkout/<int:course_id>/", views.checkout, name="checkout"),
    path("success/", views.checkout_success, name="checkout_success"),
    path("cancel/", views.payment_cancel, name="payment_cancel"),
    path("webhook/", views.stripe_webhook, name="stripe_webhook"),
]
