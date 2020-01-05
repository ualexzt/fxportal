from django.views.generic import ListView, DetailView
from blog.models import Post, Category


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-pub_date']

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    model = Post
    slug_field = 'slug'


class CategoryDetailView(DetailView):
    model = Category
    slug_field = 'slug'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = self.model.objects.all()
        context['posts'] = self.get_object().post_set.all()
        return context
