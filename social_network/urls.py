from django.urls import path
from social_network.views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name="feed"),
]