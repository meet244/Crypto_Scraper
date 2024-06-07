# Create your models here.
from django.db import models
import uuid

# Defining the Task model
class Task(models.Model):
    # Unique identifier for each task
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Status of the task, default is 'PENDING'
    status = models.CharField(max_length=20, default='PENDING')
    
    # Result of the task, stored as JSON data
    result = models.JSONField(null=True, blank=True)
