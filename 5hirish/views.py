from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import os
from django.conf import settings
from django.http import HttpResponse


def home_index(request):

    if request.method == 'GET':
        return HttpResponseRedirect('/me/')


def download_resume(request):
    file_name = 'Shirish_Sharad_Kadam_Android_0.pdf'
    file_path = os.path.join(settings.BASE_DIR, 'static/files/'+file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/x-pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponseRedirect('/me/')
