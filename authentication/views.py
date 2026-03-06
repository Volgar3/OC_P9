from django.shortcuts import render
from django.views.generic import FormView

from authentication.forms import UserCreationForm


# Create your views here.
class SigninView(FormView):
    form_class = UserCreationForm
    template_name = "authentication/sign-in.html"
