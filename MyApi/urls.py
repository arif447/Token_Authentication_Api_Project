from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'singer', SingerView, basename='singer')
router.register(r'song', SongView, basename='song')

urlpatterns = [] +router.urls