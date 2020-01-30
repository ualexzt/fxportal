from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import DiaryCategory, DiaryNote, DiarySubCatigory


class DiaryCategoryView(LoginRequiredMixin, ListView):
    model = DiaryCategory
    template_name = 'diary/diarycategory_list.html'

    def get_queryset(self):
        return DiaryCategory.objects.filter(author=self.request.user)


class DiaryCategoryDetailView(DetailView):
    model = DiaryCategory
    template_name = 'diary/diarycategory_detail.html'
    pk_url_kwarg = 'cat_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcategories'] = DiarySubCatigory.objects.filter(parent=self.object)
        return context


class DiaryCategoryCreateView(CreateView):
    model = DiaryCategory
    fields = ['name', 'cat_img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary_cat_list')


class DiaryCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DiaryCategory
    fields = ['name', 'cat_img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary_cat_list')

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


class DiarySubCategoryDetailView(DetailView):
    model = DiarySubCatigory
    template_name = 'diary/diarysubcategory_detail.html'
    pk_url_kwarg = 'sub_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = DiaryNote.objects.filter(category=self.object)
        return context


class DiarySubCategoryCreateView(CreateView):
    model = DiarySubCatigory
    fields = ['name']
    success_url = 'diary_cat_detail'

    def form_valid(self, form):
        form.instance = self.get_object().parent.name
        return super().form_valid(form)


class DiaryNoteDetailView(LoginRequiredMixin, DetailView):
    model = DiaryNote
    template_name = 'diary/diarynote_detail.html'

    def get_object(self, *args, **kwargs):
        return DiaryNote.objects.get(pk=self.kwargs.get("cat_pk"))


class DiaryNoteCreateView(CreateView):
    model = DiaryNote
    fields = ['title', 'category', 'content']
    pk_url_kwarg = 'cat_pk'

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

    def get_object(self, *args, **kwargs):
        self.kwargs.get("cat_pk")
        return DiaryNote.objects.get(pk=self.kwargs.get("cat_pk"))

    def test_func(self):
        note = self.get_object()
        print(note)
        if self.request.user == self.request.user:
            return True
        return False
