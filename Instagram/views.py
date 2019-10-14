from django.shortcuts import render
from .models import Post
from django.views.generic import  ListView,DetailView, CreateView

# Create your views here.

# def home(request):
#     context ={
#     'posts':Post.objects.all()
#     }
#     return render(request, 'index.html', context )


class PosListView(ListView):
    model = Post
    template_name = 'index.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostCreateView(CreateView):
    model = Post
    fields = ['caption']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class PostDetailView(DetailView):
    model = Post


def about(request):
    return render (request, 'about.html')
