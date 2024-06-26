from django.urls import path
from lms.apps import LmsConfig
from lms.views import ChapterCreateAPIView, ChapterListAPIView, ChapterRetrieveAPIView, ChapterUpdateAPIView, \
    ChapterDestroyAPIView, MaterialCreateAPIView, MaterialListAPIView, MaterialRetrieveAPIView, MaterialUpdateAPIView, \
    MaterialDestroyAPIView, CheckAnswerCreateAPIView, AnswerCreateAPIView

app_name = LmsConfig.name

urlpatterns = [
    path('chapter/create/', ChapterCreateAPIView.as_view(), name='chapter_create'),
    path('', ChapterListAPIView.as_view(), name='chapter_list'),
    path('chapter/view/<int:pk>/', ChapterRetrieveAPIView.as_view(), name='chapter_view'),
    path('chapter/update/<int:pk>/', ChapterUpdateAPIView.as_view(), name='chapter_update'),
    path('chapter/delete/<int:pk>/', ChapterDestroyAPIView.as_view(), name='chapter_delete'),
    path('material/create/', MaterialCreateAPIView.as_view(), name='material_create'),
    path('material/list/', MaterialListAPIView.as_view(), name='material_list'),
    path('material/view/<int:pk>/', MaterialRetrieveAPIView.as_view(), name='material_view'),
    path('material/update/<int:pk>/', MaterialUpdateAPIView.as_view(), name='material_update'),
    path('material/delete/<int:pk>/', MaterialDestroyAPIView.as_view(), name='material_delete'),
    path('check_answer/', CheckAnswerCreateAPIView.as_view(), name='check_answer'),
    path('answer/', AnswerCreateAPIView.as_view(), name='answer'),
]
