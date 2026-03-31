from django.views.generic import CreateView
from django.urls import reverse_lazy # a changer une fois que l'on a créer l'application pour gérer ce qu'il se passe après l'authentication

from authentication.forms import SignupForm


class SigninView(CreateView):
    form_class = SignupForm
    template_name = "authentication/sign-in.html"
    
    success_url = reverse_lazy('home') # a changer aussi du coup
