from django.conf.urls import url
from .views import view_project, project_detail, add_project

urlpatterns = [

    url('^$', view_project),
    url('add', add_project),
    url('^[0-9]', project_detail),
]
