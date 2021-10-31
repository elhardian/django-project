from rest_framework import generics, mixins, status, viewsets

from .models import Post
from .serializers import PostSerializer

class PostViewSet(mixins.CreateModelMixin, 
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
  
  queryset = Post.objects.all()
  serializer_class = PostSerializer
