from django.shortcuts import render, HttpResponseRedirect
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

        pro_current_str = request.POST.get("current", "False")

        if pro_current_str == "True":
            pro_current = True
        else:
            pro_current = False

        pro_title = request.POST.get("title", "")
        pro_from = date_from
        pro_to = date_to
        pro_file = request.POST.get("file_name", "")
        pro_link = request.POST.get("url_link", "")
        pro_tech = request.POST.get("tech", "")
        pro_descp = request.POST.get("description", "")

        project = AddProject(project_title=pro_title, project_start=pro_from, project_current=pro_current, project_end=pro_to,
                             project_file=pro_file, project_url=pro_link, project_tech=pro_tech, project_description=pro_descp)
        project.save()

        return render(request, 'add_project.html', {})


def edit_project(request, pid=0):

    projects = AddProject.objects.all().filter(project_id=pid)

    if request.method == 'GET':
        if len(projects) > 0:
            return render(request, 'edit_project.html', {"projects": projects})
        else:
            return HttpResponseRedirect("/projects")

    elif request.method == 'POST':
        for project in projects:

            date_from = datetime.datetime.strptime(request.POST.get("date_from", ""), "%d-%m-%Y").strftime('%Y-%m-%d')

            if request.POST.get("date_to", "") == "":
                date_to = datetime.date.today().strftime('%Y-%m-%d')
            else:
                date_to = datetime.datetime.strptime(request.POST.get("date_to", ""), "%d-%m-%Y").strftime('%Y-%m-%d')

            pro_current_str = request.POST.get("current", "False")

            if pro_current_str == "True":
                project.project_current = True
            else:
                project.project_current = False

            project.project_title = request.POST.get("title", "")
            project.project_start = date_from
            project.project_end = date_to
            project.project_file = request.POST.get("file_name", "")
            project.project_url = request.POST.get("url_link", "")
            project.project_tech = request.POST.get("tech", "")
            project.project_description = request.POST.get("description", "")

            project.save()

        return render(request, 'edit_project.html', {"projects": projects})
