from django.shortcuts import render
from .models import Post
from django.views.generic import  ListView,DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def home(request):
#     context ={
#     'posts':Post.objects.all()
#     }
#     return render(request, 'index.html', context )


class PostListView(ListView):
    model = Post
    template_name = 'index.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['caption', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['caption', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class PostDetailView(DetailView):
    model = Post


def about(request):
    return render (request, 'about.html')
