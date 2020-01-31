from django.urls import path
from .views import DiaryCategoryView, DiaryCategoryCreateView, DiaryCategoryUpdateView, \
    DiaryCategoryDeleteView, DiaryCategoryDetailView, DiaryNoteDetailView, DiaryNoteUpdateView, DiaryNoteCreateView, \
    DiarySubCategoryDetailView, DiarySubCategoryCreateView, DiarySubCategoryUpdateView, DiarySubCategoryDeleteView, \
    DiaryNoteDeleteView

urlpatterns = [
    path('', DiaryCategoryView.as_view(), name='diary_cat_list'),

    path('<int:cat_pk>/', DiaryCategoryDetailView.as_view(), name='diary_cat_detail'),
    path('create/', DiaryCategoryCreateView.as_view(), name='diary_cat_create'),
    path('<int:cat_pk>/update/', DiaryCategoryUpdateView.as_view(), name='diary_cat_update'),
    path('<int:cat_pk>/delete/', DiaryCategoryDeleteView.as_view(), name='diary_cat_delete'),

    path('<int:cat_pk>/create/', DiarySubCategoryCreateView.as_view(), name='diary_subcat_create'),
    path('<int:cat_pk>/<int:sub_pk>/', DiarySubCategoryDetailView.as_view(), name='diary_subcat_detail'),
    path('<int:cat_pk>/<int:sub_pk>/update/', DiarySubCategoryUpdateView.as_view(), name='diary_subcat_update'),
    path('<int:cat_pk>/<int:sub_pk>/delete', DiarySubCategoryDeleteView.as_view(), name='diary_subcat_delete'),

    path('<int:cat_pk>/<int:sub_pk>/<int:note_pk>/', DiaryNoteDetailView.as_view(), name='diary_note_detail'),
    path('<int:cat_pk>/<int:sub_pk>/create/', DiaryNoteCreateView.as_view(), name='diary_note_create'),
    path('<int:cat_pk>/<int:sub_pk>/<int:note_pk>/update/', DiaryNoteUpdateView.as_view(), name='diary_note_update'),
    path('<int:cat_pk>/<int:sub_pk>/<int:note_pk>/delete/', DiaryNoteDeleteView.as_view(), name='diary_note_delete')

]
