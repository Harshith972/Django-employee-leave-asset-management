from django.urls import path

from .views import (
    request_asset,
    asset_requests,
    approve_asset,
    assign_asset,
    admin_asset_requests,
)

urlpatterns = [
    path("request/", request_asset, name="request_asset"),
    path("requests/", asset_requests, name="asset_requests"),
    path("admin-requests/", admin_asset_requests, name="admin_asset_requests"),
    path("approve/<int:id>/", approve_asset, name="approve_asset"),
    path("assign/<int:id>/", assign_asset, name="assign_asset"),
]