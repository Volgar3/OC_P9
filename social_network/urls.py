from django.urls import path
from social_network.views import FeedView, TicketCreateView, ReviewCreateView, TicketAndReviewCreateView, TicketUpdateView, TicketDeleteView

# A titre perso :
# On remplie le path en mettant l'url que l'on veut avoir,
# le nom de la fonction, et le nom qu'on donne au path
# pour faire le return dans le view.py
# .asview() est nécessaire uniquement quand c'est une classe

urlpatterns = [
    path('feed/', FeedView.as_view(), name="feed"),
    path('create-ticket/', TicketCreateView.as_view(), name="create_ticket"),
    path('create-review/<int:ticket_id>/', ReviewCreateView.as_view(), name="create_review"),
    path('create-ticket-and-review/', TicketAndReviewCreateView.as_view(),name="create_ticket_and_review"),
    path('update-ticket/<int:pk>/', TicketUpdateView.as_view(), name="update_ticket"),
    path('delete-ticket/<int:pk>/', TicketDeleteView.as_view(), name="delete_ticket"),
    path('update-review/<int:pk>/', TicketUpdateView.as_view(), name="update_review"),
    path('delete-review/<int:pk>/', TicketDeleteView.as_view(), name="delete_review")

]
