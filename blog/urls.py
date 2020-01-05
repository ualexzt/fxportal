from django.urls import path
from .views import PostListView, PostDetailView, CategoryDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<category>/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>', CategoryDetailView.as_view(), name='category_detail')
]
