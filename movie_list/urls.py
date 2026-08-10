from django.urls import path
from . import views

app_name = 'movie_list'

urlpatterns = [
    path(
        'movies',
        views.movie_list,
        name='movie_list'
    ),
    path(
        'movies/<int:movie_id>/',
        views.movie_detail,
        name='movie_detail'
    ),
    path(
        'images/<str:image_name>/',
        views.display_portrait,
        name='display_portrait'
    )
]