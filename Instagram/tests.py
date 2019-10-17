from django.test import TestCase
from .models import Post
from users.models import Profile
from django.contrib.auth.models import User

# Create your tests here.


class TestPost(TestCase):
    def setUp(self):
        self.user = User(username='Ndundiro')
        self.user.save()
        self.post_test = Post(id=1,caption='no human is limited', image='default.png', user=self.user)

        


    def test_instance(self):
        self.assertTrue(isinstance(self.post_test, Post))

    def test_save_post(self):
        self.post_test.save_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_post(self):
        before = Profile.objects.all()
        self.post_test.delete_post()
        after = Profile.objects.all()
        self.assertTrue(len(before) == len(after))








    #    self.profile_test = Profile(id=2, user=self.user, bio='no human is limited', image='default.jpg' )
        # self.profile_test.save()


        # likes = post_test.likes.set([request.likes])