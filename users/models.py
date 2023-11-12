from django.db import models
from PIL import Image
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

def crop_to_square(image):
    min_size = min(image.width, image.height)
    image = image.crop((0, 0, min_size, min_size))

    return image
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            img = crop_to_square(img)
            img.save(self.image.path)

class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email': self.user.email, 'code': self.code})
        send_mail(
            'Subject here',
            'Test verification email',
            'from@example.com',
            [self.user.email],
            fail_silently=False,
        )

