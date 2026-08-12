from django.urls import path
from . import views

app_name = 'actor_list'

urlpatterns = [
    path(
        '',
        views.actor_list,
        name='actor_list'
    ),
    path(
        '<int:actor_id>/',
        views.actor_detail,
        name='actor_detail'
    )
]