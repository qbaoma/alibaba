#coding=utf-8
__author__ = 'wxy'

#1.0版本先不完成outh，留出接口，统一返回True

def auth_by_user_count(count,passw):
    #认为认证成功
    res = True
    #如果认证失败返回空得token
    if not res:
        token = ''
    #随便定义了一个token，返回
    else :
        token = 'tmp'
    return token

def auth_by_token(token):

    pass