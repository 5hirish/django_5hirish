from django.conf.urls import url
from .views import view_project

urlpatterns = [

    url('^$', view_project),
]
