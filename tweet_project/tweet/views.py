from .models import Tweet, Like, Comment
from .serializers import TweetSerializer, LikeSerializer, CommentSerializer
from rest_framework import generics

class TweetListCreate(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

class LikeRender(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
