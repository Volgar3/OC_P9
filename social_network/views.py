from itertools import chain
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import CharField, Value
from social_network.models import Ticket, Review

# Create your views here.
class FeedView(LoginRequiredMixin, TemplateView):
    template_name = "social_network/feed.html"

    def get_users_viewable_reviews(self):
        current_user = self.request.user
        return Review.objects.filter(user=current_user)

    def get_users_viewable_tickets(self):
        current_user = self.request.user
        return Ticket.objects.filter(user=current_user)

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