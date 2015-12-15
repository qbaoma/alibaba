#coding=utf-8
'''
index 的后端代码都放在这里
'''
__author__ = 'wxy'

import tornado.web
from sqlalchemy.exc import IntegrityError

from db.dbUtil import save_new_user,check_user

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")

class IndexHandler(tornado.web.RequestHandler):
    '''
    函数名称起得有些失误，本模块对应名称应该为 login
    '''

    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        '''
        1.0版本不通过outh 认证，通过查询数据库
        :param args:
        :param kwargs:
        :return:
        '''
        #print u'called'
        account = self.get_argument("account")
        passw = self.get_argument("passw")
        account = account.strip()
        passw = passw.strip()
        if passw=='' or account =='':
            self.render("login_fail.html")
        else:
            res=check_user(account,passw)
            if res:
                self.set_secure_cookie("username",account)
                self.redirect('/')
            else:
                self.render("login_fail.html")


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login_form.html')

    def post(self, *args, **kwargs):
        pass

class RegisterHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        self.render('regist_form.html')

    def post(self, *args, **kwargs):
        account = self.get_argument('account')
        passw1 = self.get_argument('passw')
        passw2 = self.get_argument('rpassw')
        if passw2.strip() != passw1.strip():
            self.redirect('regist_fail')
        else:
            account = account.strip()
            passw = passw1.strip()
            try:
                save_new_user(account,passw)
            except IntegrityError as e:
                self.redirect('regist_fail')
        self.render('regist_success.html')
        pass

class RegistFailHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        self.render('login.html')

    def get(self, *args, **kwargs):
        self.render('login.html')