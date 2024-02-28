from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ToDoNote = models.CharField(max_length=100)
    Create_Date = models.DateField(auto_now_add=True)
    Create_Time = models.TimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'ToDoNote']
        ordering = ['is_done', 'Create_Date', 'Create_Time']

    def __str__(self):
        return f'{self.ToDoNote}'
