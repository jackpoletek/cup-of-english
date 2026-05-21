from django import forms
from .models import TeacherProfile


class TeacherProfileForm(forms.ModelForm):

    class Meta:
        model = TeacherProfile
        fields = ["bio", "image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        widget = self.fields["image"].widget

        self.fields["image"].widget.clear_checkbox_label = ""
        widget.template_name = "django/forms/widgets/file.html"

    def clean_image(self):

        image = self.cleaned_data.get("image")

        if not image:
            return image

        valid_extensions = ["jpg", "jpeg", "png",]

        extension = image.name.lower()

        if not extension.endswith(tuple(valid_extensions)):
            raise forms.ValidationError(
                "Unsupported file extension. Please upload a JPG or PNG image."
            )

        if image.size > 4 * 1024 * 1024:
            raise forms.ValidationError(
                "Image file size cannot exceed 4MB."
            )

        return image
