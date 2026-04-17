from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from authentication.views import SigninView
from authentication.forms import LoginForm


urlpatterns = [
    path('', TemplateView.as_view(template_name="authentication/landing.html"),name="landing"),
    path('inscription/', SigninView.as_view(), name="sign-in"),
    path('log_out/', LogoutView.as_view(), name="logout"),
    path('log_in/', LoginView.as_view(
        template_name='authentication/login.html',
        authentication_form=LoginForm
    ), name="login"),
]
