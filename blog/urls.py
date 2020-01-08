from django.urls import path
from .views import PostListView, PostDetailView, CategoryDetailView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('comments_add/', CommentCreateView.as_view(template_name='blog/post_detail.html'), name='comment_add'),
    path('<category>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>', CategoryDetailView.as_view(), name='category_detail')

]
