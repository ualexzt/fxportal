from django.template.context_processors import request
from diary.models import DiaryCategory


def menu(request):
    diarycat = DiaryCategory.objects.all()
    return {'categories': diarycat}
