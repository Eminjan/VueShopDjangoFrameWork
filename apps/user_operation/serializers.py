#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

from rest_framework import serializers
from .models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = UserFav
        fields = ("user", "goods","id")
