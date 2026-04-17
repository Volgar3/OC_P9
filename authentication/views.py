from django.views.generic import CreateView
from django.urls import reverse_lazy

from authentication.forms import SignupForm


class SigninView(CreateView):
    form_class = SignupForm
    template_name = "authentication/sign-in.html"
    
    success_url = reverse_lazy('feed')
