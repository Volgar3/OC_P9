from itertools import chain

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.db.models import CharField, Value
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from social_network.models import Ticket, Review
from social_network.forms import TicketForm

# Create your views here.
class FeedView(LoginRequiredMixin, TemplateView):
    template_name = "social_network/feed.html"

    def get_users_viewable_reviews(self):
        """
        Retourne toutes les reviews visibles par l'utilisateur connecté :
        - ses propres reviews
        - les reviews des utilisateurs qu'il suit
        - les reviews en réponse à ses propres tickets (même si l'auteur n'est pas suivi)
        """
        current_user = self.request.user
        followed_users = current_user.following_users.values_list('followed_user', flat=True)
        return (
            Review.objects.filter(user=current_user) |
            Review.objects.filter(user__in=followed_users) |
            Review.objects.filter(ticket__user=current_user)
        ).distinct()

    def get_users_viewable_tickets(self):
        """
        Retourne tous les tickets visibles par l'utilisateur connecté :
        - ses propres tickets
        - les tickets des utilisateurs qu'il suit
        """
        current_user = self.request.user
        followed_users = current_user.following_users.values_list('followed_user', flat=True)
        return (
            Ticket.objects.filter(user=current_user) |
            Ticket.objects.filter(user__in=followed_users)
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.get_users_viewable_reviews()
        # returns queryset of reviews
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
        tickets = self.get_users_viewable_tickets()
        # returns queryset of tickets
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
        # combine and sort the two types of posts
        posts = sorted(
            chain(reviews, tickets),
            key=lambda post: post.time_created,
            reverse=True
        )
        context["posts"] = posts
        return context

# Demander une critique
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('feed')
    else:
        form = TicketForm()
    return render(request, 'social_network/create_ticket.html', {'form': form})

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ('title', 'description', 'image')
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
    