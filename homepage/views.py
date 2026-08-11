from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    template = 'homepage/index.html'
    return render(request, template)

def display_portrait(request, image_name):
    template = 'homepage/image_view.html'
    context = {'image_name': image_name}
    return render(request, template, context)