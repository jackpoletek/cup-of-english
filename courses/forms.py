from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment"]

# simple validation
def clean_rating(self):
    rating = self.cleaned_data.get("rating")
    if rating < 1 or rating > 5:
        raise forms.ValidationError("Rating must be 1-5")
    return rating
