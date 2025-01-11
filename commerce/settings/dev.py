import os

from dotenv import load_dotenv

from .share import *

# Load environment variables from .env/.dev
load_dotenv(
    os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env/.dev"
    )
)


DEBUG = True
SECRET_KEY = "django-insecure-lcivrb*$=fq(5wn+5-nwo6st51f^2!f$xoacyw0qtv^j_o#m-v"
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "commerce",
        "USER": "postgres",
        "PASSWORD": "M.j.512296",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

MAX_IMAGE_SIZE_KB = 1_000


PRODUCT_IMAGE_STORAGE_BACKEND_ACCESS_KEY = "minioadmin"
PRODUCT_IMAGE_STORAGE_BACKEND_SECRET_KEY = "minioadmin"
PRODUCT_IMAGE_STORAGE_BACKEND_BUCKET_NAME = "products-images"
PRODUCT_IMAGE_STORAGE_BACKEND_ENDPOINT_URL = "http://minio:9000"
