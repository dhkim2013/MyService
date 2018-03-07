from django.urls import path

from retube import views

urlpatterns = [
    path('', views.index),
]