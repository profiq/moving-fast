#!/usr/bin/env python
import os
import sys

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    django_env = os.environ.get("DJANGO_ENV")

    # For tests
    if sys.argv[1] == "test" or django_env == "test":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test")

    # For local development
    elif django_env == "develop":
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.develop")

    # Production
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.docker")

    execute_from_command_line(sys.argv)
