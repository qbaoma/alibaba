#coding=utf-8
'''
支付宝模块
'''
__author__ = 'wxy'
import tornado.web

from db.dbUtil import add_paypal_account
from db.dbUtil import get_balance_by_id,get_user_accounts

class CreatePayPayl(tornado.web.RequestHandler):
    '''
    创建新的支付宝账户
    '''
    #@tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.redirect('/')
        pass

    #@tornado.web.authenticated
    def post(self, *args, **kwargs):
        user_id = self.get_secure_cookie("user_id")
        user_id = int(user_id)
        money = self.get_argument("totalmoney")
        money = int(money)
        accountId = add_paypal_account(user_id,money)
        self.redirect('/account/{0}'.format(accountId))

class PayPayl(tornado.web.RequestHandler):
    '''
    查看一个支付宝账户的信息
    '''
    #@tornado.web.authenticated
    def get(self,account_id, *args, **kwargs):
        account_id = int(account_id)
        balance = get_balance_by_id(account_id)
        if balance==False:
            self.redirect('/')
        self.render('balance.html',balance=balance)

class AllPayPayl(tornado.web.RequestHandler):
    '''
    查看一个人所有的支付宝信息
    '''
    def get(self,*args, **kwargs):
        user_id = self.get_secure_cookie("user_id")
        user_id = int(user_id)
        user_accounts = get_user_accounts(user_id)
        print user_accounts
        self.render('user_accounts.html',accounts=user_accounts)







