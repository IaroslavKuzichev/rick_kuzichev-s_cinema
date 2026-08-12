from django.shortcuts import render, get_object_or_404
from .models import Actor

# Create your views here.
def actor_list(request):
    template = 'actor_list/actor_list.html'
    actors = Actor.objects.order_by('name')
    context = {'actors': actors}
    return render(request, template, context)

