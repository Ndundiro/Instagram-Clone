from django.urls import path
from . import views
from .views import PosListView

urlpatterns = [
    # path('', views.home, name='insta-home'),
    path('about/', views.about, name="insta-about"),
    path('', PosListView.as_view(), name='insta-home'),

]