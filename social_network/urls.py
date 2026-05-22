from django.urls import path
from social_network.views import FeedView, TicketCreateView
from social_network.views import create_ticket

# A titre perso :
# On remplie le path en mettant l'url que l'on veut avoir,
# le nom de la fonction, et le nom qu'on donne au path
# pour faire le return dans le view.py
# .asview() est nécessaire uniquement quand c'est une classe

    
urlpatterns = [
    path('feed/', FeedView.as_view(), name="feed"),
    path('create-ticket/', create_ticket, name="create_ticket"),
    path('create-ticket/class', TicketCreateView.as_view(), name="ticket-create")
]