from django import forms
from .models import UserRatings, UserFavorites


class RatingsForm(forms.ModelForm):
    class Meta:
        model = UserRatings
        fields = ('rating',)
        RATING_CHOICES = ((5, 5), (4, 4), (3, 3), (2, 2), (1, 1))
        widgets = {
            'rating': forms.Select(choices=RATING_CHOICES)
        }
