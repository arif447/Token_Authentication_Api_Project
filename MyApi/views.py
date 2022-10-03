from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
# Create your views here.

# we can create token for user in terminal by the command py manage.py drf_create_token username
# and admin panel in the token model we can create token without command

class SingerView(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]


class SongView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

