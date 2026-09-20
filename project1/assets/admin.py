from django.contrib import admin
from .models import AssetRequest


@admin.register(AssetRequest)
class AssetRequestAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "asset_type",
        "status",
        "assigned_asset",
    )

    search_fields = (
        "user__username",
        "asset_type",
        "assigned_asset",
    )

    list_filter = (
        "status",
        "asset_type",
    )

    ordering = (
        "status",
        "asset_type",
    )