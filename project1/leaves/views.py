from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import LeaveForm
from .models import Leave

def is_admin(user):
    return user.is_staff


@login_required
def apply_leave(request):
    if request.method == "POST":
        form = LeaveForm(request.POST)

        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            leave.save()
            return redirect("leave_history")
    else:
        form = LeaveForm()

    return render(request, "leaves/apply_leave.html", {
        "form": form
    })

@login_required
def leave_history(request):
    leaves = Leave.objects.filter(user=request.user)

    status = request.GET.get("status", "")
    date = request.GET.get("date", "")

    if status:
        leaves = leaves.filter(status=status)

    if date:
        leaves = leaves.filter(start_date=date)

    return render(
        request,
        "leaves/leave_history.html",
        {
            "leaves": leaves,
            "status": status,
            "date": date,
        }
    )

@login_required
def cancel_leave(request, leave_id):
    leave = Leave.objects.get(id=leave_id, user=request.user)

    if leave.status == "Pending":
        leave.delete()

    return redirect("leave_history")

    
@login_required
@user_passes_test(is_admin)
def approve_leave(request, id):
    leave = Leave.objects.get(id=id)
    leave.status = "Approved"
    leave.save()
    return redirect("leave_history")


@login_required
@user_passes_test(is_admin)
def reject_leave(request, id):
    leave = Leave.objects.get(id=id)
    leave.status = "Rejected"
    leave.save()
    return redirect("leave_history")

