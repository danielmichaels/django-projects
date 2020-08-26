from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import accounts.signals
