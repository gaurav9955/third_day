from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
