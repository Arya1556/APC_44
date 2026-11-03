import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "development-only-not-for-deployment")
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
ROOT_URLCONF = "urls"
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "transport",
]
MIDDLEWARE = []
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True
TIME_ZONE = "UTC"
