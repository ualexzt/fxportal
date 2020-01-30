from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from PIL import Image


class DiaryCategory(models.Model):
    name = models.CharField(default='Новый дневник', max_length=150, db_index=True, verbose_name='Название дневника')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE, verbose_name='Автор дневника')
    cat_img = models.ImageField(default='diary_img/diary.jpeg', upload_to='diary_img',
                                verbose_name='Изображение категории')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Дневник'
        verbose_name_plural = 'Дневники'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('diary_cat_detail', kwargs={'cat_pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.cat_img.path)
        output_size = (500, 500)
        img.thumbnail(output_size)
        img.save(self.cat_img.path)


class DiarySubCatigory(models.Model):
    parent = models.ForeignKey(DiaryCategory, blank=True, on_delete=models.CASCADE,
                               verbose_name='Дневник')
    name = models.CharField(max_length=100, verbose_name='Название категории')
    update_date = models.DateTimeField(auto_now=True, verbose_name='')

    class Meta:
        verbose_name = 'Категория дневника'
        verbose_name_plural = 'Категории дневника'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('diary_subcat_detail', kwargs={'main_pk': self.parent.pk, 'sub_pk': self.pk})


class DiaryNote(models.Model):
    category = models.ForeignKey(DiarySubCatigory, on_delete=models.CASCADE, verbose_name='Категория дневника')
    title = models.CharField(max_length=150, db_index=True, default='Новая заметка', verbose_name='Заметка')
    content = RichTextUploadingField(blank=True, verbose_name='Текст заметки')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('diary_note_detail',
                       kwargs={'main_pk': self.category.parent.pk, 'sub_pk': self.category.pk, 'note_pk': self.pk})
