from django import forms
from django.forms import ModelForm
from tasks.models import Task


class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "dateCompleted", "important", "fkUser"]

        widgets = {"fkUser": forms.Select(attrs={"class": "form-select"})}
