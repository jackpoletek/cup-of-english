from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    rating = forms.ChoiceField(
        choices=[
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5")
        ],
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Review
        fields = ["rating", "comment"]

        widgets = {
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),
        }

    # Simple validation inside form to ensure rating is between 1 and 5
    def clean_rating(self):

        rating = int(self.cleaned_data.get("rating"))

        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")

        return rating
