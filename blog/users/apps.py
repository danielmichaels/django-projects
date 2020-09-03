from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        """
        Import signals so they fire.
        """
        # noinspection PyUnresolvedReferences
        import users.signals
