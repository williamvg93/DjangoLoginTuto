from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from tasks.forms import AddTaskForm
from tasks.models import Task

# Create your views here.

def tasks(request):

    tasks = Task.objects.all()

    return render(
        request, "layouts/tasks/tasks.html", {"pageTitle": "Tasks", "mainPageTitle": "Tasks List", "data" : tasks}
    )


def addTask(request):

    if request.method == "GET":
        return render(
            request,
            "layouts/tasks/addTask.html",
            {"pageTitle": "AddTask", "mainPageTitle": "Add Taks", "form" : AddTaskForm},
        )
    else:
        print(request.POST)
        try:
            form = AddTaskForm(request.POST)
            newTask = form.save(commit=False)
            print(newTask.full_clean())
            print(newTask)
            newTask.save()
        except Exception as err:
            return render(
                request,
                "layouts/tasks/addTask.html",
                {
                    "pageTitle": "AddTask",
                    "mainPageTitle": "Add Taks",
                    "form": AddTaskForm,
                    "msgError": f"An Error has occurred : {err}",
                },
            )
        return render(
            request,
            "layouts/tasks/addTask.html",
            {"pageTitle": "AddTask", "mainPageTitle": "Add Taks", "form" : AddTaskForm},
        )
