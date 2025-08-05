"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

if os.getenv("RAILWAY_ENVIRONMENT") is None:
    from dotenv import load_dotenv
    from pathlib import Path
    
    BASE_DIR = Path(__file__).resolve().parent

    ENV = os.environ.get("ENV", "dev")  # default to 'dev' if not set
    dotenv_path = BASE_DIR / f".env.{ENV}"
    load_dotenv(dotenv_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv("DJANGO_SETTINGS_MODULE"))

application = get_asgi_application()
