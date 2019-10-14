from django.shortcuts import render
from .models import Post
from django.views.generic import  ListView

# Create your views here.

# def home(request):
#     context ={
#     'posts':Post.objects.all()
#     }
#     return render(request, 'index.html', context )


class PosListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


def about(request):
    return render (request, 'about.html')
