from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=50)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    class Meta:
        ordering = ["owner", "name"]

    def __str__(self):
        return self.name
