from django import template
from diary.models import DiaryCategory

register = template.Library()


@register.simple_tag(takes_context=True)
def get_categories(context):
    user = context['user']
    return DiaryCategory.objects.filter(author=user)
