from django.contrib import admin
from .models import Leave


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "leave_type",
        "start_date",
        "end_date",
        "status",
    )

    search_fields = (
        "user__username",
        "leave_type",
        "reason",
    )

    list_filter = (
        "status",
        "leave_type",
        "start_date",
    )

    ordering = (
        "-start_date",
    )