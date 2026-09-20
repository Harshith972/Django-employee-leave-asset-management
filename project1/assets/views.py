from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import AssetRequest
from .forms import AssetRequestForm


def is_admin(user):
    return user.is_staff


@login_required
def request_asset(request):
    if request.method == "POST":
        form = AssetRequestForm(request.POST)

        if form.is_valid():
            asset = form.save(commit=False)
            asset.user = request.user
            asset.save()
            return redirect("asset_requests")
    else:
        form = AssetRequestForm()

    return render(request, "assets/request_asset.html", {
        "form": form
    })


@login_required
def asset_requests(request):
    assets = AssetRequest.objects.filter(user=request.user)

    return render(request, "assets/asset_requests.html", {
        "assets": assets
    })


@login_required
@user_passes_test(is_admin)
def approve_asset(request, id):
    asset = AssetRequest.objects.get(id=id)
    asset.status = "Approved"
    asset.save()
    return redirect("admin_asset_requests")


@login_required
@user_passes_test(is_admin)
def assign_asset(request, id):
    asset = AssetRequest.objects.get(id=id)

    if request.method == "POST":
        asset.assigned_asset = request.POST["assigned_asset"]
        asset.save()
        return redirect("admin_asset_requests")

    return render(request, "assets/assign_asset.html", {
        "asset": asset
    })


@login_required
@user_passes_test(is_admin)
def admin_asset_requests(request):
    assets = AssetRequest.objects.all()

    return render(request, "assets/admin_asset_requests.html", {
        "assets": assets
    })