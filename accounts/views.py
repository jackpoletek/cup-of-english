from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Your site is up and running!')
