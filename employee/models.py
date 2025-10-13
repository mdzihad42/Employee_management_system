from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    user=[
        ('HR','HR'),
        ('SR','SR'),
    ]
    user_type=models.CharField(choices=user,null=True)
    
class DepartmentModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
class EmployeeModel(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    phone=models.CharField(max_length=20,null=True)
    department=models.ForeignKey(DepartmentModel,  null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class SalaryModel(models.Model):
    employee_image=models.ImageField(null=True,upload_to="employee_image/image")
    employee=models.OneToOneField(EmployeeModel,null=True,on_delete=models.CASCADE)
    basic_salary=models.IntegerField(null=True)
    bonus_percentage=models.IntegerField(null=True)
    total_salary=models.IntegerField(null=True)
    
    def __str__(self):
        return self.employee


