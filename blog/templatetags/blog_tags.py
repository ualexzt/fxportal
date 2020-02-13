from django import template
from ..models import Post

register = template.Library()


@register.inclusion_tag('blog/last_post.html')
def show_last_post(count=5):
    latest_post = Post.objects.order_by('-pub_date')[:count]
    return {'latest_post': latest_post}
