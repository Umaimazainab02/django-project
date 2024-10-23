from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Add_Blog(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="blogImages/",null=True, blank=True)
    
    
    title = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.title + " by " + self.created_by.username