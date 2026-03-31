from django.urls import path
from social_network.views import HomeView

urlpatterns = [
    path('home/', HomeView.as_view(), name="home"),
]