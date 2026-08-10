from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    genre = models.CharField(max_length=256, verbose_name='Жанр')
    year = models.IntegerField(verbose_name='Год')

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')

    class Meta:
        verbose_name = 'актёр'
        verbose_name_plural = 'Актёры'

    def __str__(self):
        return self.title


class Role(models.Model):
    name = models.CharField(max_length=256, verbose_name='Персонаж')
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
        verbose_name='Актёр'
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name='Фильм'
    )

    class Meta:
        verbose_name = 'роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title