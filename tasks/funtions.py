from tasks.models import Task

def GetTask(taskId):
    try:
        task = Task.objects.get(pk=taskId)
        print(task)
        print(f"id: {task.id}")
        print(type(task))
        return task
    except Exception as err:
        print(f"Error: {err}")
        print(f"Error: {str(err)}")
        print(type(str(err)))
        return str(err)
