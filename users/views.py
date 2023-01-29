from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, message=f"Welcome {username}!")
            # blog-home is a custom name I gave
            return redirect("blog-home")

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form": form})

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
