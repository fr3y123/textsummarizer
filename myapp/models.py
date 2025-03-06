from django.db import models

# Create your models here.


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)