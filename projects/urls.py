from django.conf.urls import url
from .views import view_project, project_detail, add_project, edit_project

urlpatterns = [

    url('^$', view_project),
    url('^add$', add_project),
    url('^(?P<pid>[0-9]+)$', project_detail),
    url('^(?P<pid>[0-9]+)/edit$', edit_project)
]
