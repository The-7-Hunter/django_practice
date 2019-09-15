from django.shortcuts import render, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    context = {
        "random_text": get_random_string(length=5)
    }
    return HttpResponse(f"this is random word it is { context['random_text'] }, it is your {request.session['counter']}")
    