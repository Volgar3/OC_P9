from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from authentication.views import SigninView

urlpatterns = [
    path('inscription/', SigninView.as_view(), name="sign-in"),
    path('log_out/', LogoutView.as_view(), name="logout"),
    path('log_in/', LoginView.as_view(
        template_name='authentication/login.html' # Je dois spécifier ce template car de base la fonction fournis par django s'attends à un autre path de templates
    ), name="login"),
]
