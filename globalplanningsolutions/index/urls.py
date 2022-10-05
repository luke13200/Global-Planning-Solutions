from django.urls import path

from . import views


urlpatterms = [
    path('', views.index_view, name='index')
]
