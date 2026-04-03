from django.contrib import admin
from social_network.models import UserFollows, Ticket, Review

# Register your models here.
admin.site.register(UserFollows)
admin.site.register(Ticket)
admin.site.register(Review)
