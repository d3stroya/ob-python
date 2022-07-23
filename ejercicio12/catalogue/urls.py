from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hola', views.hola, name="hola"),
    path('films', views.films, name="films"),
    path('directors', views.directors, name="directors")
]