from django.urls import path
from . import views
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    url('', include(router.urls)),
]