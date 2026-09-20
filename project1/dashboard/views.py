from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from employees.models import Employee
from leaves.models import Leave
from assets.models import AssetRequest

@login_required
def dashboard(request):
    total_employees = Employee.objects.count()
    total_leave_requests = Leave.objects.count()
    approved_leaves = Leave.objects.filter(status="Approved").count()
    pending_assets = AssetRequest.objects.filter(status="Pending").count()

    context = {
        "total_employees": total_employees,
        "total_leave_requests": total_leave_requests,
        "approved_leaves": approved_leaves,
        "pending_assets": pending_assets,
    }

    return render(request, "dashboard/dashboard.html", context)