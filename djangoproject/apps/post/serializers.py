from rest_framework import serializers
from django.http import HttpResponse

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'published_at', 'created_at', 'updated_at')
        
    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post
