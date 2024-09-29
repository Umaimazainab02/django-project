from django.db import models

# Create your models here.
class AddStudents(models.Model):
    username = models.CharField(max_length=50)
    
    full_name = models.TextField()
    
    
    
    roll_no = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.username
    
    