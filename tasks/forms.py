from django import forms
from django.forms import ModelForm
from tasks.models import Task


class UpdateTaskForm(ModelForm):

    id = forms.IntegerField(disabled=True)

    class Meta:
        model = Task
        fields = ["title", "id", "description", "dateCompleted", "important"]

    def __init__(self, *args, **kwargs):
        super(UpdateTaskForm, self).__init__(*args, **kwargs)
        self.fields["id"].disabled = True


class AddTaskForm(ModelForm):
    class Meta:
        model = Task
        # fields = ["title", "description", "dateCompleted", "important", "fkUser"]
        fields = ["title", "description", "important"]

        # widgets = {"fkUser": forms.Select(attrs={"class": "form-select"})}
