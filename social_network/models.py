from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from authentication.models import User


class Ticket(models.Model):
    # Your Ticket model definition goes here
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, max_length=2048)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # la clé User fait référence à mon user custom de l'app Authentication. donc permet de lier le ticket au user qui l'a créé


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    # Your UserFollows model definition goes here
    user = models.ForeignKey(User, related_name="following_users", on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, related_name="followed_by", on_delete=models.CASCADE)

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followers
        unique_together = ('user', 'followed_user', )
        
    def __str__(self):
        return f"{self.user.username} suit {self.followed_user.username}"
