from django.conf.urls import url
from insta.users import views as insta_views

urlpatterns = [
    ...
    url(r'^signup/$', insta_views.signup, name='signup'),
]