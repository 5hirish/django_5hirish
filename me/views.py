from django.shortcuts import render
# from django.core.mail import send_mail
# Create your views here.


def view_resume(requests):
    if requests.method == "POST":
        pass
    return render(requests, 'resume.html', {})