from django.shortcuts import render, get_object_or_404
from movie_list.models import Character
from .models import Actor
from .forms import ActorForm

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
    ).order_by('name')
    context = {'actor': actor, 'roles': roles}
    return render(request, template, context)

def actor_create(request, actor_id=None):
    template = 'actor_list/actor_form.html'
    if actor_id is not None:
        instance = get_object_or_404(Actor, id=actor_id)
    else:
        instance = None
    form = ActorForm(
        request.POST or None,
        files=request.FILES or None,
        instance=instance
    )
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, template, context)
