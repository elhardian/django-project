from django.contrib import admin
from django.urls import include, path
from djangoproject.apps.post import urls as post_urls

urlpatterns = [
    path('', include(post_urls)),
    path('admin/', admin.site.urls),
]