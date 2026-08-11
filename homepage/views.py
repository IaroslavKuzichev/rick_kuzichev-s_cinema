from django.shortcuts import render, get_object_or_404
from movie_list.models import Movie

# Create your views here.
def index(request):
    template = 'homepage/index.html'
    selected_movies = Movie.objects.filter(
        title__in=['Старлайт Парадайз', 
        'Ночной Всадник', 
        'Космический Рубеж',]
    ).order_by('year')
    context = {'selected_movies': selected_movies}
    return render(request, template, context)

def display_portrait(request, image_name):
    template = 'homepage/image_view.html'
    context = {'image_name': image_name}
    return render(request, template, context)