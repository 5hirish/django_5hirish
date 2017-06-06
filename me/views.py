from django.shortcuts import render

# Create your views here.


def view_resume(requests):
    return render(requests, 'base.html', {})