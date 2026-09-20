from django import forms
from .models import AssetRequest


class AssetRequestForm(forms.ModelForm):
    class Meta:
        model = AssetRequest
        fields = ["asset_type"]