from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from employees.models import Employee


def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        print("User registered successfully")

    return render(request, "accounts/register.html", {"form": form})

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        user = form.get_user()

        try:
            employee = Employee.objects.get(user=user)

            if not employee.is_active:
                form.add_error(None, "Your employee account is disabled.")
                return render(request, "accounts/login.html", {"form": form})

        except Employee.DoesNotExist:
            pass

        login(request, user)
        return redirect("home")

    return render(request, "accounts/login.html", {"form": form})
    
def home(request):
    return render(request, "accounts/home.html")

def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "accounts/change_password.html", {"form": form})

@login_required
def profile(request):
    if request.method == "POST":
        request.user.email = request.POST["email"]
        request.user.save()

    return render(request, "accounts/profile.html")