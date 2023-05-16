from django.db import models

# Create your models here.
class Student(models.Model):
    std_name=models.CharField(max_length=100)
    std_add=models.CharField(max_length=70)
    std_phone=models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.std_name
    
