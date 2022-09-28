from django.shortcuts import render
from rest_framework import viewsets

from . import serializers
from post import models as post_models

class PostViewset(viewsets.ModelViewSet):
    queryset = post_models.Post.objects.all()
    serializer_class = serializers.PostSerializer
