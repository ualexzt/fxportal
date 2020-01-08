from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post, Category, Comment
from .forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comments'] = self.get_object().comments.all()
        context['form'] = CommentForm()
        return context


class CategoryDetailView(DetailView):
    model = Category
    slug_field = 'slug'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = self.model.objects.all()
        context['posts'] = self.get_object().post_set.all()
        return context


class CommentCreateView(CreateView):
    model = Comment
    fields = ['object_id', 'comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.content_type = ContentType.objects.get_for_model(Post)
        return super().form_valid(form)
