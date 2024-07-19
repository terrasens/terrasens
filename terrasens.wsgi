import os
from django.core.wsgi import get_wsgi_application

# Définissez les paramètres de configuration de votre projet Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Créez l'application WSGI
application = get_wsgi_application()