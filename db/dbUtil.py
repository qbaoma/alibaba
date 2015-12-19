#coding=utf-8
__author__ = 'wxy'
import logging
import datetime

from . import Session,engine_str
from dbCreate import User,Product,PaypalAccount,ShoppingCart
from dbCreate import Transaction

dblog = logging.getLogger('db')
session = Session()
def save_new_user(account,passw):
    '''
    保存新用户
    :param account:
    :param passw:
    :return:
    '''
    #print u'执行插入测试'
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
    user = session.query(User).filter(User.account==count).all()
    try:
        user[0]
    except:
        return False
    if user[0].passw==passw:
        return user[0].id
    else:
        return False

def save_product(price,desc='',picurl=''):
    session.add(
        Product(
            price=price,desc=desc,picture=picurl
        )
    )
    session.commit()
    return True

def get_product(product_id):
    '''
    根据id 获得product 的详细信息
    :param product_id:
    :return:
    '''
    return session.query(
        Product
    ).filter(Product.id==product_id)[0]

def get_all_products():
    '''
    获得数据库中所有的产品
    :return:
    '''
    products = session.query(Product).all()
    for product in products:
        yield product

def add_paypal_account(user_id,balance):
    '''
    为用户添加新的账户,本函数不会检查user_id的合法性
    故必须保证user_id 合法
    :param user_id:
    :param balance:
    :return:
    '''
    user_id = int(user_id)
    balance = int(balance)
    account = PaypalAccount(user_id = user_id, balance = balance)
    session.add(
        account
    )
    session.commit()
    return account.id


def get_user_blances(user_id):
    '''
    获得用户当前余额
    :return:
    '''
    user_id = int(user_id)
    user_paypalAccounts = session.query(PaypalAccount).filter(
        PaypalAccount.user_id == user_id
    ).all()
    for account in user_paypalAccounts:
        yield account

def get_balance_by_id(balance_id):
    '''
    通过账户的id 获得账户余额信息
    :param balance_id:
    :return:
    '''
    balance_id = int(balance_id)
    balances = session.query(
        PaypalAccount
    ).filter(
        PaypalAccount.id == balance_id
    )
    try :
        balance = balances[0]
    except:
        return False
    return balance

def user_pay(user_id,account_id,int_money):
    '''
    用户支付
    :param user_id:
    :param account_id:
    :param int_money:
    :return:
    '''
    session = Session()
    user_id = int(user_id)
    account_id = int(account_id)
    int_money = int(int_money)
    account = session.query(
        PaypalAccount
    ).filter(PaypalAccount.user_id == user_id,
             PaypalAccount.id == account_id).all()
    account = account[0]
    balance = account.balance
    if balance < int_money:
        return False
    else:
        account.balance = balance - int_money
        session.commit()
        return True


def get_user_accounts(user_id):
    '''
    通过用户的id返回
    :param user_id:
    :return:
    '''
    user_id = int(user_id)
    accounts = session.query(
        PaypalAccount
    ).filter(
        PaypalAccount.user_id == user_id
    )
    return accounts

def add_car(product_id,user_id,buy_count):
    '''
    添加购物车
    :param product_id:
    :param user_id:
    :param buy_count:
    :return:
    '''
    product_id = int(product_id)
    user_id = int(user_id)
    buy_count = int(buy_count)
    for i in range(buy_count):
        session.add(
            ShoppingCart(
                buyer_id = user_id,product_id = product_id,
                add_time = datetime.datetime.now()
            )
        )
    session.commit()
    return 0

def get_car(user_id):
    '''
    获得用户的购物车中的物品栏
    :param user_id:
    :return:
    '''
    shopping_cars = session.query(
        ShoppingCart
    ).filter(ShoppingCart.buyer_id==user_id)
    return shopping_cars

def by_transaction(user_id,product_id,buyCount):
    '''
    购买指定数量的商品
    :param user_id:
    :param product_id:
    :param buyCount:
    :return:
    '''
    user_id = int(user_id)
    product_id = int(product_id)
    now = datetime.datetime.now()
    for i in range(buyCount):
        session.add(
            Transaction(
                buyer_id = user_id,
                product_id = product_id,
                tra_time = now
            )
        )
    session.commit()


def get_buy_history(user_id):
    '''
    获得用户的购买记录
    :param user_id:
    :return:
    '''
    user_id = int(user_id)
    return session.query(
        Transaction
    ).filter(
        Transaction.buyer_id == user_id
    ).all()
    pass
