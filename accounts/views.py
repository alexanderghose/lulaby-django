from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"  # ✅ Now in templates/registration/
    success_url = reverse_lazy("login")  # ✅ Redirects to login page after successful registration
