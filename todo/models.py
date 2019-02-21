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
    state = serializers.ChoiceField(choices=[(i, ts.value) for i, ts in enumerate(TaskState)])
    archived = models.BooleanField(default=False)
