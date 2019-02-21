from django.db import models
from rest_framework import serializers
import enum


class TaskState(enum.Enum):
    TODO = "TODO"
    STARTED = "STARTED"
    WAITING = "WAITING"
    DONE = "DONE"
    CANCELLED = "CANCELLED"


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=1, choices=[(t, t.value) for t in TaskState])
    archived = models.BooleanField(default=False)

    def __str__(self):
        return '{' + ' - '.join((self.title, self.state)) + '}'
