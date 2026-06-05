from itertools import chain

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.db.models import CharField, Value
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from social_network.forms import TicketForm, ReviewForm
from authentication.models import User
from social_network.models import Ticket, Review, UserFollows


class HomeView(LoginRequiredMixin, TemplateView):
    """
    Vue pour tous les posts des personnes suivies et les nôtres
    """
    template_name = "social_network/home.html"

    def get_users_viewable_reviews(self):
        current_user = self.request.user
        followed_users = current_user.following_users.values_list('followed_user', flat=True)
        return (
            Review.objects.filter(user=current_user) |
            Review.objects.filter(user__in=followed_users) |
            Review.objects.filter(ticket__user=current_user)
        ).distinct()

    def get_users_viewable_tickets(self):
        current_user = self.request.user
        followed_users = current_user.following_users.values_list('followed_user', flat=True)
        return (
            Ticket.objects.filter(user=current_user) |
            Ticket.objects.filter(user__in=followed_users)
        ).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.get_users_viewable_reviews()
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
        tickets = self.get_users_viewable_tickets()
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
        posts = sorted(
            chain(reviews, tickets),
            key=lambda post: post.time_created,
            reverse=True
        )
        context["posts"] = posts
        return context

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
        reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
        tickets = self.get_users_viewable_tickets()
        tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
        posts = sorted(
            chain(reviews, tickets),
            key=lambda post: post.time_created,
            reverse=True
        )
        context["posts"] = posts
        return context

# Btn "Demander une critique"
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ('title', 'description', 'image')
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

        
class TicketUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'social_network/ticket_update_form.html'
    model = Ticket
    fields = ('title', 'description', 'image')
    success_url = reverse_lazy('feed')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    success_url = reverse_lazy('feed')
    



# Btn on ticket user_followed
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('headline', 'body', 'rating')
    success_url = reverse_lazy('feed')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.ticket = Ticket.objects.get(pk=self.kwargs['ticket_id'])
        self.object.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ticket'] = Ticket.objects.get(pk=self.kwargs['ticket_id'])
        return context


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'social_network/review_update_form.html'
    model = Review
    fields = ('headline', 'body', 'rating')
    success_url = reverse_lazy('feed')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    success_url = reverse_lazy('feed')

# Btn on top of the feed "Créer une critique"
class TicketAndReviewCreateView(LoginRequiredMixin, View):
    
    def get(self, request):
        ticket_form = TicketForm()
        review_form = ReviewForm()
        return render(request, 'social_network/ticket_and_review_form.html', {
            'ticket_form': ticket_form,
            'review_form': review_form
        })
  
    def post(self, request):
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('feed')
        return render(request, 'social_network/ticket_and_review_form.html', {
            'ticket_form': ticket_form,
            'review_form': review_form
        })


class FollowersView(LoginRequiredMixin, View):

    def get(self, request):
        following = UserFollows.objects.filter(user=request.user)
        followers = UserFollows.objects.filter(followed_user=request.user)
        return render(request, 'social_network/followers.html', {
            'following': following,
            'followers': followers,
        })

    def post(self, request):
        action = request.POST.get('action')

        if action == 'follow':
            username = request.POST.get('username')
            try:
                user_to_follow = User.objects.get(username=username)
                if user_to_follow != request.user:
                    UserFollows.objects.get_or_create(user=request.user, followed_user=user_to_follow)
            except User.DoesNotExist:
                pass

        elif action == 'unfollow':
            user_id = request.POST.get('user_id')
            UserFollows.objects.filter(user=request.user, followed_user_id=user_id).delete()

        return redirect('followers')