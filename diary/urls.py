from django.urls import path
from .views import DiaryCategoryView, DiaryCategoryCreateView, DiaryCategoryUpdateView, \
    DiaryCategoryDeleteView, DiaryCategoryDetailView, DiaryNoteDetailView, DiaryNoteUpdateView, DiaryNoteCreateView

urlpatterns = [
    path('', DiaryCategoryView.as_view(), name='diary_cat_list'),
    path('<int:pk>/', DiaryCategoryDetailView.as_view(), name='diary_cat_detail'),
    path('create/', DiaryCategoryCreateView.as_view(), name='diare_cat_create'),
    path('<int:pk>/update/', DiaryCategoryUpdateView.as_view(), name='diare_cat_update'),
    path('<int:pk>/delete/', DiaryCategoryDeleteView.as_view(), name='diare_cat_delete'),
    path('note/create/', DiaryNoteCreateView.as_view(), name='diare_note_create'),
    path('note/<int:pk1>/<int:pk2>/', DiaryNoteDetailView.as_view(), name='diary_note_detail'),
    path('note/<int:pk>/update/', DiaryNoteUpdateView.as_view(), name='diary_note_update')

]
