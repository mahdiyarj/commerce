from django.core.exceptions import ValidationError

from commerce import settings


def validate_image_size(image):
    max_size_kb = settings.MAX_IMAGE_SIZE_KB

    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Images cannot be larger than {max_size_kb}KB!")
