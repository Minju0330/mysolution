from django.shortcuts import render
from .models import Content

# Create your views here.
def home(request):
    posts = Content.objects.all
    return render(request, 'home.html', {'posts_list':posts})