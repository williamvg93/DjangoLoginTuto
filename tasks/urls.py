from os import name
from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.mainPage, name="singup"),
]
