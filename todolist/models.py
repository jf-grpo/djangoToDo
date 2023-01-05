from django.db import models

# todolist/models.py
# Create your models here.

class TaskList(models.Model):
    class StatusChoice(models.TextChoices):
        TODO = "To do"
        DOING = "Doing"
        DONE = "Done"

    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=StatusChoice.choices, default=StatusChoice.TODO, max_length=100)

    def __str__(self):
        """Provides a readable reference for each object"""
        return f"{self.status}: {self.name}"

    