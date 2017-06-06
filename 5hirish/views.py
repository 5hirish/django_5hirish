from django.http import HttpResponseRedirect
from django.shortcuts import redirect


def home_index(request):

    if request.method == 'GET':
        return HttpResponseRedirect('/me/')
