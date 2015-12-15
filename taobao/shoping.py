#coding=utf-8
'''
本文件为用户的各种购物行为提供支持
'''
__author__ = 'wxy'
import tornado.web
from sqlalchemy.exc import IntegrityError

from db.dbUtil import get_all_products,save_product
from index import BaseHandler


class WelcomeHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("welcome.html",user=self.current_user)

class LogoutHandler(BaseHandler):
    def get(self, *args, **kwargs):
        print u'logoutcalled'
        self.clear_cookie("username")
        self.redirect('/login')

class ProductHandler(tornado.web.RequestHandler):
    '''
    如果请求执行到这个类，则性能一定会有损失，因为可能之前也查询了数据库
    '''
    def get(self,*args, **kwargs):
        products = get_all_products()
        self.render('products.html',products=products)

        pass

    def post(self,*args, **kwargs):
        price = self.get_argument(u"price",u'')
        if price =='':
            self.redirect('/')
        desc = self.get_argument(u"desc",u'')
        picurl = self.get_argument(u"url",u'')
        save_product(price,desc,picurl)
        self.redirect('/')
        pass

