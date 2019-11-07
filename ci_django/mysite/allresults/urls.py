from django.urls import path

from . import views

urlpatterns = [
    path('', views.allresults, name='allresults'),
]