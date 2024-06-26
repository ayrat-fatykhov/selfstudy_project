from django.db import models

from config import settings


NULLABLE = {'blank': True, 'null': True}


class Question(models.Model):
    """
    Определяет поля для модели Вопрос.
    """
    question = models.CharField(max_length=255, verbose_name='вопрос')
    right_answer = models.CharField(max_length=255, verbose_name='правильный ответ')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Вопрос.
        """
        return f'{self.question}, {self.right_answer}'

    class Meta:
        """
        Определяет отображение модели Вопрос в админке. Сортирует по порядковому номеру.
        """
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'
        ordering = ('pk',)


class Answer(models.Model):
    """
    Определяет поля для модели Ответ.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        **NULLABLE
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос')
    user_answer = models.CharField(max_length=255, verbose_name='ответ пользователя')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Ответ.
        """
        return f'{self.user}, {self.question}, {self.user_answer}'

    class Meta:
        """
        Определяет отображение модели Ответ в админке. Сортирует по порядковому номеру.
        """
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
        ordering = ('pk',)


class CheckAnswer(models.Model):
    """
    Определяет поля для модели Проверка Ответа.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='вопрос')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='ответ пользователя')
    is_right = models.BooleanField(default=False, verbose_name='ответ верный')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Проверка Ответа.
        """
        return f'{self.question}, {self.answer}, {self.is_right}'

    class Meta:
        """
        Определяет отображение модели Проверка Ответа в админке. Сортирует по порядковому номеру.
        """
        verbose_name = 'проверка ответа'
        verbose_name_plural = 'проверки ответов'
        ordering = ('pk',)


class Chapter(models.Model):
    """
    Определяет поля для модели Раздел.
    """
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Раздел.
        """
        return f'{self.name}, {self.description}'

    class Meta:
        """
        Определяет отображение модели Раздел в админке. Сортирует по порядковому номеру.
        """
        verbose_name = 'раздел'
        verbose_name_plural = 'разделы'
        ordering = ('pk',)


class Material(models.Model):
    """
    Определяет поля для модели Материал.
    """
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name='раздел')
    questionnaire = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name='опросник', **NULLABLE)

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Материал.
        """
        return f'{self.name}, {self.description}, {self.chapter}'

    class Meta:
        """
        Определяет отображение модели Материал в админке. Сортирует по порядковому номеру.
        """
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
        ordering = ('pk',)
