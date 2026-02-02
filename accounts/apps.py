from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

def ready(self):
        """
        This method is called when Django starts. It imports the signals module
        to ensure that signal handlers are connected.
        """
        import accounts.signals
