from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()