from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.tasks, name="tasks"),
    path("taskCompleted/", views.lTasksCompleted, name="taskCompleted"),
    path("tasksPending/", views.lTasksPending, name="tasksPending"),
    path("addTask/", views.addTask, name="addTask"),
    path("taskSearch/", views.taskSearch, name="taskSearch"),
    path("updateTask/", views.updateTask, name="updateTask"),
    path("completeTask/<int:taskId>", views.completedTask, name="completeTask"),
    path("deleteTask/<int:taskId>/", views.deleteTask, name="deleteTask"),
]
