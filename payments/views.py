import stripe
import json
import logging
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from accounts.models import User
from courses.models import Course
from enrollments.models import Enrollment

logger = logging.getLogger(__name__)

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

        metadata={
            "user_id": request.user.id,
            "course_id": course.id,
        },

        success_url=request.build_absolute_uri("/payments/success/"),
        cancel_url=request.build_absolute_uri("/payments/cancel/"),
    )

    return redirect(session.url)


# Success and cancel views
def payment_success(request):
    return render(request, "payments/payment_success.html")


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

        user_id = session.get("metadata", {}).get("user_id")
        course_id = session.get("metadata", {}).get("course_id")

        try:
            user = User.objects.get(id=user_id)
            course = Course.objects.get(id=course_id)

            # Prevent duplicate enrollments
            if not Enrollment.objects.filter(user=user, course=course).exists():
                Enrollment.objects.create(
                    user=user,
                    course=course,
                )
                logger.info(f"Enrollment created for user {user} and course {course}")

        except Exception as e:
            logger.exception("Webhook error: %s", e)
            return HttpResponse(status=500)

    return HttpResponse(status=200)
