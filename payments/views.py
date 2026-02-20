from django.shortcuts import render


def checkout(request):
    return render(request, "payments/checkout.html")

def checkout_success(request):
    return render(request, "payments/checkout_success.html")

def payment_cancel(request):
    return render(request, "payments/payment_cancel.html")

def payment_success(request):
    return render(request, "payments/payment_success.html")
