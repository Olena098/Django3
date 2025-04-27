from django.db import models
from django.utils import timezone
from django.db.models.functions import Now

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    
    # варіант 1 — через Python функцію
    publish = models.DateTimeField(default=timezone.now)

    # або варіант 2 — через SQL функцію (починаючи з Django 5.0+)
    # publish = models.DateTimeField(db_default=Now())

    def __str__(self):
        return self.title
