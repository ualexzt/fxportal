from django.urls import path
from .views import DiaryCategoryView, DiaryCategoryCreateView, DiaryCategoryUpdateView, \
    DiaryCategoryDeleteView, DiaryCategoryDetailView, DiaryNoteDetailView, DiaryNoteUpdateView, DiaryNoteCreateView, \
    DiarySubCategoryDetailView, DiarySubCategoryCreateView

urlpatterns = [
    path('', DiaryCategoryView.as_view(), name='diary_cat_list'),

    path('<int:cat_pk>/', DiaryCategoryDetailView.as_view(), name='diary_cat_detail'),
    path('create/', DiaryCategoryCreateView.as_view(), name='diare_cat_create'),
    path('<int:cat_pk>/update/', DiaryCategoryUpdateView.as_view(), name='diare_cat_update'),
    path('<int:cat_pk>/delete/', DiaryCategoryDeleteView.as_view(), name='diare_cat_delete'),

    path('sub_add/', DiarySubCategoryCreateView.as_view(), name='diary_subcat_create'),
    path('<int:main_pk>/<int:sub_pk>/', DiarySubCategoryDetailView.as_view(), name='diary_subcat_detail'),



    path('note/<int:cat_pk>/create/', DiaryNoteCreateView.as_view(), name='diare_note_create'),
    path('note/<int:cat_pk>/<int:note_pk>/', DiaryNoteDetailView.as_view(), name='diary_note_detail'),
    path('note/<int:cat_pk>/<int:note_pk>/update/', DiaryNoteUpdateView.as_view(), name='diary_note_update')

]
