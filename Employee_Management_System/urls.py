
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Employee_Management_System.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('department/',departmentPage,name="department"),
    path('departmentDlt/<int:id>',departmentDlt,name="departmentDlt"),
    path('departmentEdit/<int:id>',departmentEdit,name="departmentEdit"),
    
    path('employee/',employeePage,name="employee"),
    path('employeeDlt/<int:id>',employeeDlt,name="employeeDlt"),
    path('employeeEdit/<int:id>',employeeEdit,name="employeeEdit"),
    
    path('salary/',salaryPage,name="salary"),
    path('salaryDlt/<int:id>',salaryDlt,name="salaryDlt"),
    path('salaryEdit/<int:id>',salaryEdit,name="salaryEdit"),
    
    path('',basePage,name="base"),
    
    path('loginPage/',loginPage,name="loginPage"),
    path('signupPage/',signupPage,name="signupPage"),
    path('logoutPage/',logoutPage,name="logoutPage")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
