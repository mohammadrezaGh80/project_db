from django.shortcuts import render

from .forms import CustomUserCreationForm
from .models import CustomUser


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = f"{user.first_name}_{CustomUser.objects.last().id + 1}"
            user.save()
            return render(request, "accounts/successful_signup.html", context={"username": user.username})
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", context={"form": form})
