from django.contrib import admin
from .models import DiaryCategory, DiaryNote, DiarySubCategory

admin.site.register(DiaryCategory)
admin.site.register(DiarySubCategory)
admin.site.register(DiaryNote)
