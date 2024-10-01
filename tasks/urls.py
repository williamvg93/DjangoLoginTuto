from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.tasks, name="tasks"),
    path("addTask/", views.addTask, name="addTask"),
    path("taskSearch/", views.taskSearch, name="taskSearch"),
    path("updateTask/", views.updateTask, name="updateTask"),
    path("deleteTask/<int:taskId>/", views.deleteTask, name="deleteTask"),
]
