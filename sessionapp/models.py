from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_name=models.CharField(max_length=100)
    Emp_address=models.CharField(max_length=80)
    Emp_phone=models.CharField(max_length=20)
    
    def __str__(self):
        return self.Emp_name
    
