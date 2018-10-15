#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M


import requests


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        params = {
            "api_key": self.api_key,
            "mobile": mobile,
            "text": "【慕学生鲜】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)

        }
        response = requests.post(self.single_send_url, data=params)
        import json
        re_dict = json.loads(response.text)
        print(re_dict)


if __name__ == '__main__':
    yun_pian = YunPian("dee0ae688dd65917f37911516afa6f54")
    yun_pian.send_sms("2018", "15327648069")
