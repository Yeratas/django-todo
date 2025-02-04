from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True)
    completion = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['completion']
        
    def __str__(self):
            return self.title    