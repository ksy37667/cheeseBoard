from django.shortcuts import render

from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.response import Response

from .models import Post


# Create your views here.
class PostListGenericAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    