from django.urls import path

from . import views

urlpatterns = [
    path('', views.timelog, name='v'),
]