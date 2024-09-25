from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from tasks.forms import AddTaskForm
from tasks.models import Task
from tasks.funtions import GetTask

# Create your views here.


def tasks(request):

    # tasks = Task.objects.all()
    tasks = Task.objects.filter(fkUser=request.user)

    return render(
        request,
        "layouts/tasks/tasks.html",
        {"pageTitle": "Tasks", "mainPageTitle": "Tasks List", "data": tasks},
    )


def addTask(request):

    if request.method == "GET":
        return render(
            request,
            "layouts/tasks/addTask.html",
            {"pageTitle": "AddTask", "mainPageTitle": "Add Taks", "form": AddTaskForm},
        )
    else:
        print(request.POST)
        try:
            form = AddTaskForm(request.POST)
            newTask = form.save(commit=False)
            newTask.fkUser = request.user
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
            {"pageTitle": "AddTask", "mainPageTitle": "Add Taks", "form": AddTaskForm},
        )


def taskDetail(request, taskId):
    print(taskId)
    try:
        task = Task.objects.get(pk=taskId)
        print(task)
        return render(
            request,
            "layouts/tasks/searchTask.html",
            {"pageTitle": "TaskDetail", "mainPageTitle": "Taks Detail", "data": task},
        )
    except Exception as err:
        print(f"Error: {err}")
        return render(
            request,
            "layouts/tasks/searchTask.html",
            {
                "pageTitle": "TaskDetail",
                "mainPageTitle": "Taks Detail",
                "msgError": f"An Error has occurred : {err}",
            },
        )


def taskSearch(request):
    dataPage = {
            "pageTitle": "TaskDetail",
            "mainPageTitle": "Taks Detail",
    }
    if request.POST:
        if "TId" in request.POST:
            data = GetTask(request.POST["TId"])
            if isinstance(data, str):
                dataPage["msgError"] = data
            else:
                dataPage["data"] = data
            return render(request, "layouts/tasks/searchTask.html", dataPage)

        if "taskId" in request.POST:
            print(request.POST)
            data = GetTask(request.POST["taskId"])
            if isinstance(data, str):
                dataPage["msgError"] = data
            else:
                dataPage["data"] = data
            return render(request, "layouts/tasks/searchTask.html", dataPage)
    else:
        return render(request, "layouts/tasks/searchTask.html", dataPage)
