from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """ 
    This class configures the accounts app and handles initialisation tasks
    such as importing signals when the app is ready.
    """

    # Specifies the default auto-generated primary key field type
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        # Import signals to ensure they are registered when the app is ready
        import accounts.signals  # noqa: F401
