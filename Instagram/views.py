from django.shortcuts import render
from .models import Post
from django.views.generic import  ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect

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


class PostDetailView(DetailView):
    model = Post


    


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['caption', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['caption', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/instagram'
    


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


def about(request):
    return render (request, 'about.html')

    #################################################################################
    


@login_required(login_url='/login/')
def likePost(request,image_id):

   image = Post.objects.get(pk = image_id)

   is_liked = False
   if image.likes.filter(id = request.user.id).exists():
       image.likes.remove(request.user)
       is_liked = False
   else:
       image.likes.add(request.user)
       is_liked = True

   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




#############################comment attempt 4###################
# @login_required(login_url='/accounts/login/')
# def comment_on(request, post_id):
#     commentform = CommentForm()
#     post = get_object_or_404(Post, pk=post_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.user = request.user.profile
#             comment.photo = post
#             comment.save()
#     return render(request, 'post.html', {'form':commentform}, locals())
