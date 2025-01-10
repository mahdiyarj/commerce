from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class ProductImageStorage(S3Boto3Storage):
    file_overwrite = False
    bucket_name = settings.PRODUCT_IMAGE_STORAGE_BACKEND_BUCKET_NAME
    access_key = settings.PRODUCT_IMAGE_STORAGE_BACKEND_ACCESS_KEY
    secret_key = settings.PRODUCT_IMAGE_STORAGE_BACKEND_SECRET_KEY
    endpoint_url = settings.PRODUCT_IMAGE_STORAGE_BACKEND_ENDPOINT_URL
