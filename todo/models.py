from django.db import models


class Task(models.Model):
    TODO = 'T'
    STARTED = 'S'
    WAITING = 'W'
    DONE = 'D'
    CANCELLED = 'C'
    TASK_STATE_CHOICES = (
        (TODO, 'TODO'),
        (STARTED, 'STARTED'),
        (WAITING, 'WAITING'),
        (DONE, 'DONE'),
        (CANCELLED, 'CANCELLED')
    )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=1, choices=TASK_STATE_CHOICES, default=TODO, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.title, self.state)

    def toggle_archived(self):
        self.archived = not self.archived
        self.save()


def toggle_archived(task_id, archive):
    task = Task.objects.filter(archived=not archive).filter(id=task_id).get()
    task.archived = archive
    task.save()
