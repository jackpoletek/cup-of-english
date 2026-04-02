import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from courses.models import Course

stripe.api_key = settings.STRIPE_SECRET_KEY


# Checkout view
def checkout(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "gbp",
                "product_data": {
                    "name": course.title,
                },
                "unit_amount": int(course.price * 100),
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url=request.build_absolute_uri("/payments/success/"),
        cancel_url=request.build_absolute_uri("/payments/cancel/"),
    )

    return redirect(session.url)

# Success and cancel views
def checkout_success(request):
    return render(request, "payments/checkout_success.html")

def payment_cancel(request):
    return render(request, "payments/payment_cancel.html")


# Stripe webhook to handle events (e.g. payment success)
@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)
    except Exception:
        return HttpResponse(status=400)

    # Handle payment success
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        print("Payment successful:", session.id)

    return HttpResponse(status=200)
