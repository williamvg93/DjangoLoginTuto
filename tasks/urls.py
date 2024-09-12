from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.tasks, name="tasks"),
    path("addTask/", views.addTask, name="addTask"),
    # path("<int:taskId>/", views.taskDetail, name="taskDetail"),
    path("taskSearch/", views.taskSearch, name="taskSearch"),
]
