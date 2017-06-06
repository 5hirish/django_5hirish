from django.conf.urls import url
from .views import view_resume

urlpatterns = [

    url('^$', view_resume),
]
