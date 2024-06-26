from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from lms.models import Chapter, Material, CheckAnswer
from lms.serializers import ChapterSerializer, MaterialSerializer, CheckAnswerSerializer, AnswerSerializer
from users.permissons import IsModer


class ChapterCreateAPIView(generics.CreateAPIView):
    """
    Отвечает за создание нового Раздела
    """
    serializer_class = ChapterSerializer
    permission_classes = [IsModer]


class ChapterListAPIView(generics.ListAPIView):
    """
    Отвечает за отображение списка Разделов
    """
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ChapterRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отвечает за отображение одного Раздела
    """
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ChapterUpdateAPIView(generics.UpdateAPIView):
    """
    Отвечает за редактирование Раздела
    """
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()
    permission_classes = [IsModer]


class ChapterDestroyAPIView(generics.DestroyAPIView):
    """
    Отвечает за удаление Раздела
    """
    queryset = Chapter.objects.all()
    permission_classes = [IsModer]


class MaterialCreateAPIView(generics.CreateAPIView):
    """
    Отвечает за создание нового Материала
    """
    serializer_class = MaterialSerializer
    permission_classes = [IsModer]


class MaterialListAPIView(generics.ListAPIView):
    """
    Отвечает за отображение списка Материалов
    """
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('chapter',)


class MaterialRetrieveAPIView(generics.RetrieveAPIView):
    """
    Отвечает за отображение одного Материла
    """
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()


class MaterialUpdateAPIView(generics.UpdateAPIView):
    """
    Отвечает за редактирование Материала
    """
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    permission_classes = [IsModer]


class MaterialDestroyAPIView(generics.DestroyAPIView):
    """
    Отвечает за удаление Материала
    """
    queryset = Material.objects.all()
    permission_classes = [IsModer]


class CheckAnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = CheckAnswerSerializer

    def perform_create(self, serializer):
        check_answer = serializer.save()
        if check_answer.answer.user_answer.lower() == check_answer.question.right_answer.lower():
            check_answer.is_right = True
        check_answer.save()


class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        answer = serializer.save()
        answer.user = self.request.user
        answer.save()
