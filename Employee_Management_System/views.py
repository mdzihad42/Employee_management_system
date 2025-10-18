from django.shortcuts import render,redirect
from employee.models import*
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

@login_required
def departmentPage(request):
    if request.method=="POST":
        DepartmentModel.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description")
        )
        return redirect('department')
    return render(request,"department.html",
                {'department':DepartmentModel.objects.all()}
                )
    
@login_required
def departmentDlt(request,id):
    DepartmentModel.objects.get(id=id).delete()
    return redirect('department')
def departmentEdit(request,id):
    department_data=DepartmentModel.objects.get(id=id)
    if request.method=="POST":
        id=id
        department_data.name=request.POST.get("name")
        department_data.description=request.POST.get("description")
        department_data.save()
        
        return redirect('department')
    return render(request,"departmentedit.html",
                {'department':DepartmentModel.objects.all(),
                'department_data':DepartmentModel.objects.get(id=id)
                }
                )

@login_required
def employeePage(request):
    if request.method=="POST":
        EmployeeModel.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            department=DepartmentModel.objects.get(id=request.POST.get("department"))
        )
        
        return redirect('employee')
    return render(request,"employee.html",
                
                {
                'department':DepartmentModel.objects.all(),
                'employee':EmployeeModel.objects.all()   
                }
                )

@login_required
def employeeDlt(request,id):
    EmployeeModel.objects.get(id=id).delete()
    return redirect('employee')

@login_required
def employeeEdit(request,id):
    employee_data=EmployeeModel.objects.get(id=id)
    if request.method=="POST":
        department_data=DepartmentModel.objects.get(id=request.POST.get("department"))
        id=id
        employee_data.name=request.POST.get("name")
        employee_data.email=request.POST.get("email")
        employee_data.phone=request.POST.get("phone")
        employee_data.department=department_data
        employee_data.save()
        return redirect('employee')
    return render(request,"employeedit.html",
                
                {
                'department':DepartmentModel.objects.all(),
                'employee_data':EmployeeModel.objects.get(id=id),
                'employee':EmployeeModel.objects.all()   
                }
                )
def salaryPage(request):
    if request.method=="POST":
        basic_salary=int(request.POST.get("basic_salary"))
        bonus_percentage=int(request.POST.get("bonus_percentage"))
        total=int(basic_salary + (basic_salary *bonus_percentage / 100))
        
        SalaryModel.objects.create(
            employee_image=request.FILES.get("employee_image"),
            employee=EmployeeModel.objects.get(id=request.POST.get("employee")),
            basic_salary=basic_salary,
            bonus_percentage=bonus_percentage,
            total_salary=total
        )
        return redirect('salary')
    return render(request,"salary.html",
                {
                    'salary':SalaryModel.objects.all(),
                    'employee':EmployeeModel.objects.all()
                }
                )
def salaryDlt(request,id):
    SalaryModel.objects.get(id=id).delete()
    return redirect('salary')
def salaryEdit(request,id):
    salary_data=SalaryModel.objects.get(id=id)
    if request.method=="POST":
        basic_salary=int(request.POST.get("basic_salary"))
        bonus_percentage=int(request.POST.get("bonus_percentage"))
        total=int(basic_salary + (basic_salary *bonus_percentage / 100))
        employee_id=EmployeeModel.objects.get(id=request.POST.get("employee"))
        employee_image=request.FILES.get("employee_image")
        if employee_image:
            salary_data.employee_image=employee_image
        id=id
        salary_data.employee=employee_id
        salary_data.basic_salary=basic_salary
        salary_data.bonus_percentage=bonus_percentage
        salary_data.total_salary=total
        salary_data.save()
        return redirect('salary')
    return render(request,"salaryedit.html",
                {
                    'salary':SalaryModel.objects.all(),
                    'employee':EmployeeModel.objects.all(),
                    'salary_data':SalaryModel.objects.get(id=id)
                }
                )
@login_required   
def basePage(request):
    salary=SalaryModel.objects.all()
    employee=EmployeeModel.objects.all()
    context={
                    'salary':salary,
                    'employee':employee
                }
    return render(request,"base.html",context)
def signupPage(request):
    user_exists=False
    if request.method=="POST":
        choose_user=request.POST.get("choose_user")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if user_exists:
            return render(request, "sign.html", {'user_exists': True})
        if password==confirm_password:
            customUser.objects.create_user(
                user_type=choose_user,
                username=username,
                email=email,
                password=confirm_password
            )
            return redirect('loginPage')
    return render(request,"sign.html",{'user_exists': user_exists})
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user= authenticate(request,username=username,password=password)
        
        if user:
            login(request,user)
            return redirect('base')
        
    return render(request,"login.html")
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

    
