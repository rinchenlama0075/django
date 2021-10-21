from django.urls import path

from . import views

appName = 'help'

urlpatterns = [
    path('', views.indexView, name='index'),
]
