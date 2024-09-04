from django.urls import path
from users.views import *

urlpatterns = [
    path("", signUp, name="signUp"),
    path("logout/", logout_user, name="logout"),
    path("signIn/", signIn, name="signIn"),
]
