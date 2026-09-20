from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm

@login_required
def profile(request):
    employee = Employee.objects.get(user=request.user)

    return render(request, "employees/profile.html", {
        "employee": employee
    })

@login_required
def edit_profile(request):
    employee = Employee.objects.get(user=request.user)

    if request.method == "POST":
        form = EmployeeForm(
            request.POST,
            request.FILES,
            instance=employee
        )

        if form.is_valid():
            form.save()
            return redirect("employee_profile")
    else:
        form = EmployeeForm(instance=employee)

    return render(request, "employees/edit_profile.html", {
        "form": form
    })

@login_required
def employee_list(request):
    employees = Employee.objects.all()

    search = request.GET.get("search", "")
    department = request.GET.get("department", "")

    if search:
        employees = employees.filter(
            user__username__icontains=search
        )

    if department:
        employees = employees.filter(
            department__icontains=department
        )

    return render(request, "employees/employee_list.html", {
        "employees": employees,
        "search": search,
        "department": department,
    })