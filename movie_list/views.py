from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Movie, Role

# Create your views here.
def movie_list(request):
    template = 'movie_list/movie_list.html'
    movies = Movie.objects.order_by('year')[::-1]
    context = {'movies': movies}
    return render(request, template, context)

def movie_detail(request, movie_id):
    template = 'movie_list/movie_detail.html'
    context = dict()
    return render(request, template, context)

def display_portrait(request, image_name):
    template = 'movie_list/image_view.html'
    context = {'image_name': image_name, 'root': settings.MEDIA_ROOT}
    return render(request, template, context)