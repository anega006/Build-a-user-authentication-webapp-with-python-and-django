"""
WSGI config for User_Authentication_Webapp_with_Python_and_Django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'User_Authentication_Webapp_with_Python_and_Django.settings')

application = get_wsgi_application()
