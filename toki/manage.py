#!/usr/bin/env python
from logging import getLogger
import os
import sys

logger = getLogger('management_commands')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "toki.settings")

    from django.core.management import execute_from_command_line

    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        logger.error('Admin Command Error: %s', ' '.join(sys.argv), exc_info=sys.exc_info())
        raise e
