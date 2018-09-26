#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

from goods.models import Goods
from goods.serializers import GoodsSerializer
from rest_framework import serializers
from trade.models import ShoppingCart,OrderInfo,OrderGoods


class ShopCartDetailSerializer(serializers.ModelSerializer):
    # 一条购物车关系记录对应的只有一个goods
    goods = GoodsSerializer(many=False,read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ('goods','nums')



# class ShopCartSerializer(serializers.Serializer):
#     user = serializers.