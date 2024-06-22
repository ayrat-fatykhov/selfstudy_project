from django.db import models


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

    def __str__(self):
        """
        Выводит информацию об экземпляре класса Материал.
        """
        return f'{self.name}, {self.description}'

    class Meta:
        """
        Определяет отображение модели Материал в админке. Сортирует по порядковому номеру.
        """
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
        ordering = ('pk',)
