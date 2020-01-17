from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post, Category, Comment
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 2

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


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'category', 'image_post', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


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
