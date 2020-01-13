from django.urls import path
from .views import PostListView, PostDetailView, CategoryDetailView, CommentCreateView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('comments_add/', CommentCreateView.as_view(template_name='blog/post_detail.html'), name='comment_add'),
    path('<category>/post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<slug:slug>', CategoryDetailView.as_view(), name='category_detail')

]
