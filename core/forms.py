from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):

    # Simple CAPTCHA field to prevent spam
    captcha = forms.IntegerField(
        label="What is 3 + 4?",
        required=True,
        min_value=0
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    def clean_captcha(self):
        captcha_answer = self.cleaned_data.get('captcha')

        if captcha_answer != 7:
            raise forms.ValidationError(
                "Incorrect answer to the CAPTCHA question."
                )

        return captcha_answer
