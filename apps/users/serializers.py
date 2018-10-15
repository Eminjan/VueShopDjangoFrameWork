#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

import re
from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta
from .models import VerifyCode

from MxShop.settings import REGEX_MOBILE
User = get_user_model()

class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """
        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if re.match(REGEX_MOBILE,mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证发送频率
        one_minute_ago = datetime.now()-timedelta(hours=0,minutes=1,seconds=0)
        if VerifyCode.objects.filter(add_time__gt = one_minute_ago,code=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60秒")

        return mobile
