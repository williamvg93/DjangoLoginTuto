from django.contrib import admin
from tasks.models import *
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    # Agregar los campos que queremos Ver de este modelo(tabla) en el Admin
    list_display = ("id", "title", "created" , "fkUser")

    # Mostrar campo en el formualrio pero solo en modo lectura
    readonly_fields = ("created",)

    search_fields = ("id", "title")

admin.site.register(Task, TaskAdmin)
