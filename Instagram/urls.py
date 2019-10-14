from django.urls import path
from . import views
from .views import PosListView, PostDetailView, PostCreateView

urlpatterns = [
    # path('', views.home, name='insta-home'),
    path('about/', views.about, name="insta-about"),
    path('', PosListView.as_view(), name='insta-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),

]