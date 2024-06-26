from rest_framework import serializers

from lms.models import Chapter, Material, CheckAnswer, Answer


class ChapterSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность. Для модели Раздел.
    """
    class Meta:
        model = Chapter
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность. Для модели Материал.
    """
    class Meta:
        model = Material
        fields = '__all__'


class CheckAnswerSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность. Для модели Проверка Ответа.
    """
    class Meta:
        model = CheckAnswer
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    """
    Переводит структуру данных в битовую последовательность. Для модели Ответ.
    """
    class Meta:
        model = Answer
        fields = '__all__'
