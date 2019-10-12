from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    caption = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.caption
