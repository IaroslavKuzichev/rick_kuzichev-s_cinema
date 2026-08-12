from django.shortcuts import render, get_object_or_404
from .models import Actor
from movie_list.models import Character

# Create your views here.
def actor_list(request):
    template = 'actor_list/actor_list.html'
    actors = Actor.objects.order_by('name')
    context = {'actors': actors}
    return render(request, template, context)

def actor_detail(request, actor_id):
    template = 'actor_list/actor_detail.html'
    actor = get_object_or_404(
        Actor,
        id=actor_id
    )
    roles = Character.objects.filter(
        actor=actor_id
    )
    context = {'actor': actor, 'roles': roles}
    return render(request, template, context)
