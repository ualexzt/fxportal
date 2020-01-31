from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import DiaryCategory, DiaryNote, DiarySubCategory


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
        context['subcategories'] = DiarySubCategory.objects.filter(parent=self.object)
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
    pk_url_kwarg = 'cat_pk'

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
    pk_url_kwarg = 'cat_pk'

    def get_success_url(self):
        return reverse('diary_cat_list')

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
            return True
        return False


class DiarySubCategoryDetailView(DetailView):
    model = DiarySubCategory
    template_name = 'diary/diarysubcategory_detail.html'
    pk_url_kwarg = 'sub_pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = DiaryNote.objects.filter(category=self.object)
        return context


class DiarySubCategoryCreateView(CreateView):
    model = DiarySubCategory
    fields = ['name']

    def form_valid(self, form):
        form.instance.parent = DiaryCategory.objects.get(pk=self.kwargs['cat_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary_cat_detail', kwargs={'cat_pk': self.kwargs['cat_pk']})


class DiarySubCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DiarySubCategory
    fields = ['name']
    pk_url_kwarg = 'sub_pk'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary_cat_detail', kwargs={'cat_pk': self.kwargs['cat_pk']})

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.parent.author:
            return True
        return False


class DiarySubCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DiarySubCategory
    pk_url_kwarg = 'sub_pk'

    def get_success_url(self):
        return reverse('diary_cat_detail', kwargs={'cat_pk': self.kwargs['cat_pk']})

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.parent.author:
            return True
        return False


class DiaryNoteDetailView(LoginRequiredMixin, DetailView):
    model = DiaryNote
    template_name = 'diary/diarynote_detail.html'


class DiaryNoteCreateView(CreateView):
    model = DiaryNote
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.category = DiarySubCategory.objects.get(pk=self.kwargs['sub_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary_subcat_detail', kwargs={'cat_pk': self.kwargs['cat_pk'], 'sub_pk': self.kwargs['sub_pk']})


class DiaryNoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DiaryNote
    fields = ['title', 'content']
    pk_url_kwarg = 'note_pk'

    def form_valid(self, form):
        form.instance.category = DiarySubCategory.objects.get(pk=self.kwargs['sub_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('diary_subcat_detail', kwargs={'cat_pk': self.kwargs['cat_pk'], 'sub_pk': self.kwargs['sub_pk']})

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.category.parent.author:
            return True
        return False


class DiaryNoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DiaryNote
    pk_url_kwarg = 'note_pk'

    def get_success_url(self):
        return reverse('diary_subcat_detail', kwargs={'cat_pk': self.kwargs['cat_pk'], 'sub_pk': self.kwargs['sub_pk']})

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.category.parent.author:
            return True
        return False
