from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя категории')
    slug = models.SlugField(unique=True, verbose_name='Ссылка категории')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
    image_post = models.ImageField(default='post_img/default_post.jpg', upload_to='post_img',
                                   verbose_name='Изображение поста')
    content = models.TextField(max_length=None, verbose_name='Текст поста')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    likes = models.PositiveIntegerField(default=0, verbose_name='Нравится')
    dislikes = models.PositiveIntegerField(default=0, verbose_name='Не нравится')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'category': self.category.slug, 'slug': self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
