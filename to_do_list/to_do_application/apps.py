from django.apps import AppConfig


class ToDoApplicationConfig(AppConfig):
    """
    Application config set by startapp.
    Name of Django Application == to_do_application.
    Automatic model Field == django.db.models.BigAutoField.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'to_do_application'
