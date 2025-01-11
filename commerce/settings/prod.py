import os

from dotenv import load_dotenv

from .share import *

# Load environment variables from .env/.prod
load_dotenv(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env/.prod"
    )
)


DEBUG = False
SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT", "5432"),
    }
}

MAX_IMAGE_SIZE_KB = int(os.environ.get("MAX_IMAGE_SIZE_KB", 5000))


PRODUCT_IMAGE_STORAGE_BACKEND_ACCESS_KEY = os.environ["STORAGE_ACCESS_KEY"]
PRODUCT_IMAGE_STORAGE_BACKEND_SECRET_KEY = os.environ["STORAGE_SECRET_KEY"]
PRODUCT_IMAGE_STORAGE_BACKEND_BUCKET_NAME = os.environ["STORAGE_BUCKET_NAME"]
PRODUCT_IMAGE_STORAGE_BACKEND_ENDPOINT_URL = os.environ["STORAGE_ENDPOINT_URL"]


SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
