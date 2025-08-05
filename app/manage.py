#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

if os.getenv("RAILWAY_ENVIRONMENT") is None:
    from dotenv import load_dotenv
    from pathlib import Path
    
    BASE_DIR = Path(__file__).resolve().parent

    ENV = os.environ.get("ENV", "dev")  # default to 'dev' if not set
    dotenv_path = BASE_DIR / f".env.{ENV}"
    load_dotenv(dotenv_path)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv("DJANGO_SETTINGS_MODULE"))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
