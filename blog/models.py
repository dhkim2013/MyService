from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    createdAt = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-createdAt',)