from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    caption = models.TextField()
    image = models.ImageField(upload_to = 'images', default = 'default.jpg')
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name= 'likes', blank = True)

    def total_likes(self):
       self.likes.count()
    
    
    def __str__(self):
        return self.caption


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})





class Comment(models.Model):
    text = models.TextField()
    photo = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)


    def __str__(self):
        return self.profile


    

