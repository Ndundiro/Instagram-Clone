from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='insta-home'),
    path('about/', views.about, name="insta-about"),


]