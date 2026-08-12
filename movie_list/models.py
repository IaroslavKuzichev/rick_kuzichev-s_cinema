from django.db import models
from actor_list.models import Actor

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    genre = models.CharField(max_length=256, verbose_name='Жанр')
    year = models.IntegerField(verbose_name='Год')

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'Фильмы'

    def __str__(self):
        return self.title


class Character(models.Model):
    name = models.CharField(max_length=256, verbose_name='Персонаж')
    actor = models.ForeignKey(
        Actor,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Актёр'
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        verbose_name='Фильм'
    )

    class Meta:
        verbose_name = 'персонаж'
        verbose_name_plural = 'Персонажи'

    def __str__(self):
        return self.name