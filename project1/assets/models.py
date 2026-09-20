from django.db import models
from django.contrib.auth.models import User


class AssetRequest(models.Model):

    ASSET_TYPES = [
        ("Laptop", "Laptop"),
        ("Monitor", "Monitor"),
        ("Keyboard", "Keyboard"),
        ("Headset", "Headset"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPES)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )
    assigned_asset = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.asset_type}"