from django.urls import path
from users.views import *

urlpatterns = [
    path('', signUp, name='signUp'),
]
