from django.shortcuts import render
from .models import AddProject
import datetime
# Create your views here.


def view_project(requests):

    projects = AddProject.objects.all()

    return render(requests, 'project.html', {'projects': projects})


def project_detail(requests):
    return render(requests, 'detail_project.html', {})


def add_project(request):
    if request.method == 'GET':
        return render(request, 'add_project.html', {})

    elif request.method == 'POST':

        date_from = datetime.datetime.strptime(request.POST.get("date_from", ""), "%d-%m-%Y").strftime('%Y-%m-%d')

        if request.POST.get("date_to", "") == "":
            date_to = datetime.date.today().strftime('%Y-%m-%d')
        else:
            date_to = datetime.datetime.strptime(request.POST.get("date_to", ""), "%d-%m-%Y").strftime('%Y-%m-%d')

        pro_title = request.POST.get("title", "")
        pro_from = date_from
        pro_to = date_to
        pro_file = request.POST.get("file_name", "")
        pro_link = request.POST.get("url_link", "")
        pro_tech = request.POST.get("tech", "")
        pro_descp = request.POST.get("description", "")

        project = AddProject(project_title=pro_title, project_start=pro_from, project_end=pro_to, project_file=pro_file, project_url=pro_link, project_tech=pro_tech, project_description=pro_descp)
        project.save()

        return render(request, 'add_project.html', {})
