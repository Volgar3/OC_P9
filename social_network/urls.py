from django.urls import path
from social_network.views import (
    FeedView,
    HomeView,
    TicketCreateView,
    ReviewCreateView,
    TicketAndReviewCreateView,
    TicketUpdateView,
    ReviewUpdateView,
    TicketDeleteView,
    ReviewDeleteView,
    FollowersView
)

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('feed/', FeedView.as_view(), name="feed"),
    path('home/', HomeView.as_view(), name="home"),
    path(
        'create-ticket/',
        TicketCreateView.as_view(),
        name="create_ticket"
    ),
    path(
        'create-review/<int:ticket_id>/',
        ReviewCreateView.as_view(),
        name="create_review"
    ),
    path(
        'create-ticket-and-review/',
        TicketAndReviewCreateView.as_view(),
        name="create_ticket_and_review"
    ),
    path(
        'update-ticket/<int:pk>/',
        TicketUpdateView.as_view(),
        name="update_ticket"
    ),
    path(
        'delete-ticket/<int:pk>/',
        TicketDeleteView.as_view(),
        name="delete_ticket"
    ),
    path(
        'update-review/<int:pk>/',
        ReviewUpdateView.as_view(),
        name="update_review"
    ),
    path(
        'delete-review/<int:pk>/',
        ReviewDeleteView.as_view(),
        name="delete_review"
    ),
    path('followers', FollowersView.as_view(), name="followers"),
]
