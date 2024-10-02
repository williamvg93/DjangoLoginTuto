from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.tasks, name="tasks"),
    path("taskCompleted/", views.tasksCompleted, name="taskCompleted"),
    path("tasksPending/", views.tasksPending, name="tasksPending"),
    path("addTask/", views.addTask, name="addTask"),
    path("taskSearch/", views.taskSearch, name="taskSearch"),
    path("updateTask/", views.updateTask, name="updateTask"),
    path("deleteTask/<int:taskId>/", views.deleteTask, name="deleteTask"),
]
