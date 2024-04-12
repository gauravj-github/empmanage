from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    employeename = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=200)
    age = models.IntegerField(max_length=50, default='0')  # Adding default value
    salary = models.IntegerField(default=0)
    employeeresume = models.FileField(upload_to="EmployeResume/", default='default_resume.pdf')
    empphoto = models.FileField(upload_to="EmployeResume/", default='default_resume.pdf')
    
    def __str__(self):
        return self.phone
    
class Registration(models.Model):
     user = models.ForeignKey(User, on_delete=models.SET_NULL , null = True , blank = True)


     def __str__(self):
        return self.id

class Fail(models.Model):
    p=models.CharField(max_length=11)
