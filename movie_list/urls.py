from django.urls import path
from . import views

app_name = 'movie_list'

urlpatterns = [
    path(
        '',
        views.movie_list,
        name='movie_list'
    ),
    path(
        '<int:movie_id>/',
        views.movie_detail,
        name='movie_detail'
    ),
    path(
        'create/movie/',
        views.movie_create,
        name='movie_create'
    ),
    path(
        'create/character/',
        views.character_create,
        name='character_create'
        )
]