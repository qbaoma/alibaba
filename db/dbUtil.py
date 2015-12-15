#coding=utf-8
__author__ = 'wxy'
import logging
import datetime

from . import Session,engine_str
from dbCreate import User,Product

dblog = logging.getLogger('db')

def save_new_user(account,passw):
    '''
    保存新用户
    :param account:
    :param passw:
    :return:
    '''
    #print u'执行插入测试'
    session = Session()
    account = account.strip()
    passw = passw.strip()
    has_user = session.query(User).filter(User.account==account)
    time = datetime.datetime.now()
    session.add(User(
        account = account,passw=passw,registTime = time
    ))
    session.commit()
    return 0

def check_user(count,passw):
    '''
    检查用户是否为登录用户
    :param count:
    :param passw:
    :return:
    '''
    session = Session()
    user = session.query(User).filter(User.account==count).all()
    try:
        user[0]
    except:
        return False
    if user[0].passw==passw:
        return True
    else:
        return False

def save_product(price,desc='',picurl=''):
    session = Session()
    session.add(
        Product(
            price=price,desc=desc,picture=picurl
        )
    )
    session.commit()
    return True

def get_all_products():
    '''
    获得数据库中所有的产品
    :return:
    '''
    session = Session()
    products = session.query(Product).all()
    for product in products:
        yield product
