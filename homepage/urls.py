from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'images/<str:image_name>/',
        views.display_portrait,
        name='display_portrait'
    )
]