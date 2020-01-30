from django.contrib import admin
from .models import DiaryCategory, DiaryNote, DiarySubCatigory

admin.site.register(DiaryCategory)
admin.site.register(DiarySubCatigory)
admin.site.register(DiaryNote)
