from django.apps import AppConfig


class PostAppConfig(AppConfig):
    name = 'djangoproject.apps.post'
    label = 'post'
    verbose_name = 'post'

default_app_config = 'djangoproject.apps.post.PostAppConfig'
