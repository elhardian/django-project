
import os
import importlib

# by default use development
ENV_ROLE = os.getenv('ENV_ROLE', 'base')

env_settings = importlib.import_module(f'djangoproject.settings.{ENV_ROLE}')

globals().update(vars(env_settings))

try:
  # import local settings if present
  from .local import *  # noqa
except ImportError:
  pass