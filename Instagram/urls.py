from django.urls import path
from . import views
from .views import PosListView, PostDetailView

urlpatterns = [
    # path('', views.home, name='insta-home'),
    path('about/', views.about, name="insta-about"),
    path('', PosListView.as_view(), name='insta-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

]