from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse


def generate_activation_link(request, user):
    """
    Generates a secure activation link for a user account.
    This link includes a unique token and a base64-encoded user ID.
    """

    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    activation_path = reverse("accounts:activate", kwargs={
        "uidb64": uid,
        "token": token,
    })

    return request.build_absolute_uri(activation_path)
