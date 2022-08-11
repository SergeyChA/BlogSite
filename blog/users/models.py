from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='пользователь', on_delete=models.CASCADE)
    img = models.ImageField('фото', default='default.webp', upload_to='profile_img')
    sex = models.CharField('пол', null=True, max_length=20)
    agreement = models.BooleanField('соглашение', null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    def __str__(self):
        return self.user.username
