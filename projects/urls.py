from django.conf.urls import url
from .views import view_project, project_detail

urlpatterns = [

    url('^$', view_project),
    url('^[0-9]', project_detail),
]
