from django.db import models
from users.models import User

class Album(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Photo(models.Model):
    tweet_id    = models.BigIntegerField()
    tweet_text  = models.TextField()
    tweet_likes = models.IntegerField()
    image_url   = models.URLField(max_length=255, unique=True) 
    created_at  = models.DateField(auto_now_add=True)
    album       = models.ForeignKey(Album)
    user        = models.ForeignKey(User)

    def __str__(self):
        return self.image_url