from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile_view(request):
    return render(request, "registration/profile.html", {"user": request.user})

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"  # ✅ Now in templates/registration/
    success_url = reverse_lazy("login")  # ✅ Redirects to login page after successful registration
