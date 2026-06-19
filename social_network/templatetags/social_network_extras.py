from django import template
from social_network.models import Review

register = template.Library()


@register.simple_tag
def has_reviewed(user, ticket):
    return Review.objects.filter(user=user, ticket=ticket).exists()
