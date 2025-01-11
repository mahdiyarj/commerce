from django.core.exceptions import ValidationError

from commerce.settings import share


def validate_image_size(image):
    max_size_kb = share.MAX_IMAGE_SIZE_KB

    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Images cannot be larger than {max_size_kb}KB!")
