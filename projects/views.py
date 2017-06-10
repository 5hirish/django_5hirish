from django.shortcuts import render

# Create your views here.


def view_project(requests):
    return render(requests, 'project.html', {})


def project_detail(requests):
    return render(requests, 'detail_project.html', {})