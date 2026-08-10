from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Movie, Actor, Character

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Character)