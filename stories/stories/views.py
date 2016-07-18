from django.shortcuts import render


def home(request, *args, **kwargs):
    return render(request, 'index.html', {})


def facebook_auth_start(request, *args, **kwargs):
    return
