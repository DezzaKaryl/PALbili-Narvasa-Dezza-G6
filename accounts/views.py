from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import role_required
from .forms import RegistrationForm, ProfileForm


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = RegistrationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now log in.")
            return redirect("login")
        messages.error(request, "Please fix the errors below.")
    return render(request, "accounts/register.html", {"form": form})


@login_required
def dashboard(request):
    """Sends each user to the dashboard that matches their role."""
    routes = {
        "customer": "customer_dashboard",
        "rider": "rider_dashboard",
        "admin": "admin_dashboard",
    }
    return redirect(routes[request.user.role])


@role_required("customer")
def customer_dashboard(request):
    return render(request, "accounts/customer_dashboard.html")


@role_required("rider")
def rider_dashboard(request):
    return render(request, "accounts/rider_dashboard.html")


@role_required("admin")
def admin_dashboard(request):
    return render(request, "accounts/admin_dashboard.html")


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


@login_required
def profile_edit(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile was updated.")
            return redirect("profile")
        messages.error(request, "Could not update your profile. Check the errors below.")
    return render(request, "accounts/profile_edit.html", {"form": form})