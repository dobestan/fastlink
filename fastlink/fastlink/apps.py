from django.apps import AppConfig


class FastlinkAppConfig(AppConfig):
    name = 'fastlink'

    def ready(self):
        from .signals.post_save import post_save_resource
