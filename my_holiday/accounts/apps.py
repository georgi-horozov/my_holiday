from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "my_holiday.accounts"

    def ready(self):
        import my_holiday.accounts.signals

