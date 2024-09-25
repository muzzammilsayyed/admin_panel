
# Create your models here.
from django.db import models
from django.utils import timezone

class Partner(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.name
