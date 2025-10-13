from django.contrib import admin
from employee.models import*
admin.site.register([DepartmentModel,EmployeeModel,SalaryModel,customUser])