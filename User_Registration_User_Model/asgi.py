"""
ASGI config for User Registration User Model project.
It exposes the ASGI callable as a module-level variable named ``asgi_application``.
For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""
import os

from django.core.asgi import get_asgi_application

DJANGO_SETTINGS_MODULE = 'User_Registration_User_Model.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

asgi_application = get_asgi_application()
