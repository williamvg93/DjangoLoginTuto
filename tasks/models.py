from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    dateCompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    fkUser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")

    def __str__(self):
        return self.title
