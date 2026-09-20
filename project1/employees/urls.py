from django.urls import path
from .views import profile, edit_profile, employee_list

urlpatterns = [
    path("", employee_list, name="employee_list"),
    path("profile/", profile, name="employee_profile"),
    path("edit-profile/", edit_profile, name="edit_profile"),
]