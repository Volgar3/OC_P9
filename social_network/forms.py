from django import forms
from social_network.models import Ticket, Review



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'body', 'rating']
        labels = {
            'headline': 'Titre',
            'body': 'Commentaire',
            'rating': 'Note',
        }
        # Delete txt in placeholder
        widgets = {
            'headline': forms.TextInput(attrs={'placeholder': ''}),
            'body': forms.Textarea(attrs={'placeholder': ''}),
            'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(6)]),
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        labels = {
            'title': 'Titre',
            'description': 'Description',
            'image': 'Image',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': ''}),
            'description': forms.Textarea(attrs={'placeholder': ''}),
        }
