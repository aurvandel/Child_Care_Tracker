from django.apps import AppConfig
from .task import notify_users


class TrackerConfig(AppConfig):
    name = 'tracker'

