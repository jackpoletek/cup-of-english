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
        """
        Method called when the application is fully loaded.

        Importing signals here ensures they are registered and connected
        when Django starts, preventing race conditions and ensuring
        signal handlers are active for the entire application lifecycle.
        """
    # Import signals module to connect signal handlers
        import accounts.signals
