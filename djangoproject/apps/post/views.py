from rest_framework import viewsets, response, status

from .models import Post
from .serializers import PostSerializer

class DestroyWithPayloadMixin(object):
  def destroy(self, *args, **kwargs):
    serializer = self.get_serializer(self.get_object())
    super().destroy(*args, **kwargs)
    return response.Response(serializer.data, status=status.HTTP_200_OK)

class PostViewSet(DestroyWithPayloadMixin, viewsets.ModelViewSet):
  
  queryset = Post.objects.all()
  serializer_class = PostSerializer
