#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

import requests

def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://132.232.209.153:8000/complete/weibo/"
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_uri={re_url}".format(client_id=4207750620,re_url=redirect_url)

    print(auth_url)


def get_access_token(code="4658bc7ed423058e1b4fa23aa7f964f0"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    re_dict = requests.post(access_token_url,data={
        "client_id":4207750620,
        "client_secret":"310bf5f4877331e363a2bdc56382b8ee",
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":"http://132.232.209.153:8000/complete/weibo/"
    })
    #b'{"access_token":"2.00EFtZSGUJSlaE9570f1b68deCARIE","remind_in":"157679999","expires_in":157679999,"uid":"5771324254","isRealName":"true"}'

    pass


def get_user_info(aaccess_token="",uid=""):
    user_url = "https://api.weibo.com/2/users/show.json?access_token={token}&uid={uid}".format(token=aaccess_token,uid=uid)

    print(user_url)



if __name__ == '__main__':
    # get_auth_url()
    # get_access_token(code="4658bc7ed423058e1b4fa23aa7f964f0")

    get_user_info(aaccess_token="2.00EFtZSGUJSlaE9570f1b68deCARIE",uid="5771324254")