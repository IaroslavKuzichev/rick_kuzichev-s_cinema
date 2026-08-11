from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Movie, Character

# Create your views here.
def movie_list(request):
    template = 'movie_list/movie_list.html'
    movies = Movie.objects.order_by('year')[::-1]
    context = {'movies': movies}
    return render(request, template, context)

def movie_detail(request, movie_id):
    template = 'movie_list/movie_detail.html'
    movie = get_object_or_404(
        Movie,
        id=movie_id
    )
    characters = Character.objects.select_related('actor').filter(
        movie=movie_id
    )
    context = {'movie': movie, 'characters': characters}
    return render(request, template, context)
