from django.db import models
from PIL import Image

from django.contrib.auth.models import AbstractUser

def crop_to_square(image):
    min_size = min(image.width, image.height)
    image = image.crop((0, 0, min_size, min_size))

    return image
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            img = crop_to_square(img)
            img.save(self.image.path)
