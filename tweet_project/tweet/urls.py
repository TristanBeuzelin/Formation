from django.urls import path
from . import views

urlpatterns = [
    path('', views.TweetListCreate.as_view()),
]