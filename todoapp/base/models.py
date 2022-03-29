from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null =True)
    email = models.EmailField(unique=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Task(models.Model):

    STATUS_CHOICE = [
    ('C', 'PENDING'),
    ('P', 'COMPLETED'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='tasks')
    title = models.CharField(max_length=200)
    status = models.CharField(max_length = 10, choices=STATUS_CHOICE)
    due_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

