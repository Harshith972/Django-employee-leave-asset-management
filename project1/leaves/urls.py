from django.urls import path
from .views import apply_leave, leave_history, cancel_leave,approve_leave, reject_leave

urlpatterns = [
    path("apply/", apply_leave, name="apply_leave"),
    path("history/", leave_history, name="leave_history"),
    path("cancel/<int:leave_id>/", cancel_leave, name="cancel_leave"),
    path("approve/<int:id>/", approve_leave, name="approve_leave"),
    path("reject/<int:id>/", reject_leave, name="reject_leave"),
]