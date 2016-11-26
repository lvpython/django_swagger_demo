#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.settings.dev")
    os.environ.setdefault("DATABASE_NAME", "variants_dictionary")
    os.environ.setdefault("DATABASE_USER", "dict_user")
    os.environ.setdefault("DATABASE_PASSWORD", "ymfxgdcd")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
