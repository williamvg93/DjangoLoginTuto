import re
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from tasks.forms import AddTaskForm, UpdateTaskForm
from tasks.models import Task
from tasks.funtions import GetTask
from django.utils import timezone

# Create your views here.


def tasks(request):

    # tasks = Task.objects.all()
    tasks = Task.objects.filter(fkUser=request.user)

    return render(
        request,
        "layouts/tasks/tasks.html",
        {"pageTitle": "Tasks", "mainPageTitle": "Tasks List", "data": tasks},
    )


def lTasksCompleted(request):

    # tasks = Task.objects.all()
    tasks = Task.objects.filter(fkUser=request.user, dateCompleted__isnull=False)

    return render(
        request,
        "layouts/tasks/tasks.html",
        {"pageTitle": "Tasks", "mainPageTitle": "Tasks List", "data": tasks},
    )


def lTasksPending(request):

    # tasks = Task.objects.all()
    tasks = Task.objects.filter(fkUser=request.user, dateCompleted__isnull=True)

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
            return redirect('tasks')
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
        if "taskId" in request.POST:
            print(request.POST)
            data = GetTask(request.POST["taskId"])
            if isinstance(data, str):
                dataPage["msgError"] = data
            else:
                dataPage["data"] = data
            return render(request, "layouts/tasks/searchTask.html", dataPage)
        else:
            dataPage["msgError"] = "no task id received"
            return render(request, "layouts/tasks/searchTask.html", dataPage)
    else:
        return render(request, "layouts/tasks/searchTask.html", dataPage)


def updateTask(request):
    taskId = None
    dataPage = {
            "pageTitle": "UpdateTask", "mainPageTitle": "Update Task"
    }

    if request.method == "POST":
        if "id" in request.POST:
            print(request.POST)
            taskId = request.POST["id"]

    data = GetTask(taskId)

    if isinstance(data, str):
        dataPage["msgError"] = data
    else:
        if request.method == "POST":
            if "_method" in request.POST:
                print(request.POST["_method"])
                taskId = request.POST["id"]
                data = GetTask(taskId)
                formData = UpdateTaskForm(request.POST, instance=data)
                try:
                    formData.save()
                    return redirect('tasks')
                except Exception as e:
                    dataPage["msgError"] = f"Ocurrió un error: {e}"
                    dataPage["form"] = UpdateTaskForm(instance=data)
                    return render(request, "layouts/tasks/updateTask.html", dataPage)
        formData = UpdateTaskForm(instance=data)
        dataPage["form"] = formData
    return render(request, "layouts/tasks/updateTask.html", dataPage)


def completedTask(request, taskId):
    if request.method == "POST":
        task = Task.objects.get(id=taskId, fkUser=request.user)
        task.dateCompleted = timezone.now()
        task.save()
        return redirect('tasks')
    else:
        raise Http404


def deleteTask(request, taskId):
    if request.method == "POST":
        task = GetTask(taskId)
        task.delete()
        return redirect('tasks')
    else:
        raise Http404
