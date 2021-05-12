from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Tweet(models.Model):
    text = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    likes_count = models.IntegerField(default=0, null=False, blank=False, editable=False)
    comment_count = models.IntegerField(default=0, null=False, blank=False, editable=False)

    def __str__(self):
        return self.text

class Like(models.Model):
    tweet = models.ForeignKey('Tweet', related_name='like', on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet.text

class Comment(Tweet):
    parent = models.ForeignKey('Tweet', related_name='comments',on_delete=models.CASCADE)

    def __str__(self):
        return self.text

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)