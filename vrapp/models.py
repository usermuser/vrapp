from django.db import models
from django.utils import timezone

class Process(models.Model):
    name = models.TextField(max_length=50)
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()
    duration = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True)

