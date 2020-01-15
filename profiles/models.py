from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class CategoryLearnGroup(models.Model):
    learn_category = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.learn_category

    class Meta:
        verbose_name = 'Группа обучения'
        verbose_name_plural = 'Группы обучения'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profiles_img', verbose_name='Изображение профиля')
    description = models.CharField(max_length=150, default='', verbose_name='О себе')
    categiry_learn = models.ForeignKey(CategoryLearnGroup, on_delete=models.SET_NULL, null=True, blank=True,
                                       verbose_name='Группа обучения')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
