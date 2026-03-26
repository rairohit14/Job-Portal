from django.db import models

# Create your models here.

# model job_portal

from django.db import models
from django.contrib.auth.models import User



# model job_portal
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
# Apply job feature

class Apply(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username