from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from .models import UserFav
from utils.permissions import IsOwnerOrReadOnly
from .serializers import UserFavSerializer


# Create your views here.


class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    用户收藏功能
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UserFavSerializer

    def get_queryset(self):
        return UserFav.objects.filter(user = self.request.user)
