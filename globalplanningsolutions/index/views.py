from django.shortcuts import render
from django.http import HttpResponse


def index_view(request):
    return HttpResponse(render(request, 'index/index.html', None))
