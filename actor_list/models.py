from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    date_of_birth = models.DateField(default='01.01.2000', verbose_name='Дата рождения')
    bio = models.TextField(verbose_name='Биография')
    portrait = models.ImageField(null=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'актёр'
        verbose_name_plural = 'Актёры'

    def __str__(self):
        return self.name