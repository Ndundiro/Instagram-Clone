from django.urls import path
from django.conf.urls import url
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # path('', views.home, name='insta-home'),
    # path('like/<int:pk>',views.likePost, name="likePost"),
    url(r'^like/(\d+)',views.likePost, name="likePost"),
    path('about/', views.about, name="insta-about"),
    path('', PostListView.as_view(), name='insta-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]