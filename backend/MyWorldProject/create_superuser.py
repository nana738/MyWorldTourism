import os
import django

# ✅ MUST be set BEFORE django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyWorldProject.settings")

# ✅ Initialize Django
django.setup()

# ✅ IMPORTS ONLY AFTER setup()
from django.contrib.auth import get_user_model

User = get_user_model()

USERNAME = "admin"
EMAIL = "admin@gmail.com"
PASSWORD = "admin123"

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD
    )
    print("Superuser created")
else:
    print("Superuser already exists")
