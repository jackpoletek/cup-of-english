from urllib import request

from django.shortcuts import render
import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


def checkout(request):
    return render(request, "payments/checkout.html")

def checkout_success(request):
    return render(request, "payments/checkout_success.html")

def payment_cancel(request):
    return render(request, "payments/payment_cancel.html")

def payment_success(request):
    return render(request, "payments/payment_success.html")

@csrf_exempt
def stripe_webhook(request):
    import json

    payload = request.body

    try:
        event = json.loads(payload.decode("utf-8"))
    except Exception:
        return HttpResponse(status=400)

    # Handle event
    if event["type"] == "payment_intent.succeeded":
        print("Payment succeeded")

    return HttpResponse(status=200)
