from django import template
from diary.models import DiaryCategory

register = template.Library()


@register.simple_tag()
def get_categories():
    return DiaryCategory.objects.all()
