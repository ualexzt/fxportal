from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import DiaryCategory, DiaryNote


class DiaryCategoryView(LoginRequiredMixin, ListView):
    model = DiaryCategory
    template_name = 'diary/diarycategory_list.html'

    def get_queryset(self):
        return DiaryCategory.objects.filter(author=self.request.user)


class DiaryCategoryDetailView(DetailView):
    model = DiaryCategory
    template_name = 'diary/diarycategory_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = self.get_object().diarynote_set.all()
        return context


class DiaryCategoryCreateView(CreateView):
    model = DiaryCategory
    fields = ['diary_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary_list')


class DiaryCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DiaryCategory
    fields = ['diary_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary_list')

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
            return True
        return False


class DiaryCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DiaryCategory

    def get_success_url(self):
        return reverse('diary_cat_list')

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
            return True
        return False


class DiaryNoteDetailView(LoginRequiredMixin, DetailView):
    model = DiaryNote
    template_name = 'diary/diarynote_form.html'

    def get_object(self, *args, **kwargs):
        return DiaryNote.objects.get(pk=self.kwargs.get("pk2"))


class DiaryNoteCreateView(CreateView):
    model = DiaryNote
    fields = ['title', 'category', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary_note_detail')


class DiaryNoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DiaryNote
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary_note_detail')

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.category.author:
            return True
        return False
