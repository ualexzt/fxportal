from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class DiaryCategory(models.Model):
    diary_name = models.CharField(max_length=150, verbose_name='Название дневника')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='Автор дневника')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Дневник'
        verbose_name_plural = 'Дневники'

    def get_absolute_url(self):
        return reverse('diarycategory_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.diary_name


class DiaryNote(models.Model):
    category = models.ForeignKey(DiaryCategory, on_delete=models.CASCADE, verbose_name='Дневник')
    title = models.CharField(max_length=150, default='Новая заметка', verbose_name='Заметка')
    content = RichTextUploadingField(blank=True, verbose_name='Текст заметки')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('diary_note_detail', kwargs={'pk1': self.category.pk, 'pk2': self.pk})
