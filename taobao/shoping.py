#coding=utf-8
'''
本文件为用户的各种购物行为提供支持
'''
__author__ = 'wxy'
import tornado.web
from sqlalchemy.exc import IntegrityError

from db.dbUtil import get_all_products,save_product
from db.dbUtil import get_user_blances,add_car
from db.dbUtil import get_car,get_user_accounts,user_pay
from db.dbUtil import get_product,by_transaction
from db.dbUtil import get_buy_history
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

class BuyProduct(tornado.web.RequestHandler):
    '''
    执行购买某一个商品的请求
    '''

    def post(self, *args, **kwargs):
        product_id = self.get_argument(u"product_id")
        buy_count = self.get_argument(u"buyCount")
        user_id = self.get_secure_cookie(u"user_id")
        product_id = int(product_id)

        buy_count = int(buy_count)
        user_id = int(user_id)
        #首先获得商品的单价，再获得用户所有的支付宝账户
        #print u'用户购买'
        accounts = get_user_accounts(user_id)
        #用户当前剩余金额
        rem =0
        product = get_product(product_id)
        for account in accounts:
            if account.balance < product.price*buy_count:
                pass
            else:
                by_transaction(
                    user_id,product_id,buy_count
                )
                user_pay(user_id,account.id,product.price*buy_count)
                self.redirect('/buy_history')
                break
        self.render('addAccount.html')

class AddShoppingCart(tornado.web.RequestHandler):
    '''
    将单一的商品添加至购物车
    '''
    def post(self, *args, **kwargs):
        user_id = self.get_secure_cookie("user_id")
        user_id = int(user_id)
        product_id = self.get_argument("product_id")
        product_id = int(product_id)
        buyCount = self.get_argument("buyCount")
        buyCount = int(buyCount)
        add_car(product_id,user_id,buyCount)
        self.redirect('/car')

class Car(tornado.web.RequestHandler):
    '''
    查看当前用户购物车
    '''
    def get(self, *args, **kwargs):
        user_id = self.get_secure_cookie("user_id")
        user_id = int(user_id)
        shopping_cars = get_car(user_id)
        #下面语句对返回的shopping_cars 执行了预处理
        #目的是为了渲染页面，保持页面的简洁
        #构造了一个字典，字典的 key 是物品的id
        #value 为 物品的个数
        tmp = dict()
        for shopping_car in shopping_cars:
            tmp[shopping_car.product_id]=(
                tmp[shopping_car.product_id]+1
            ) if tmp.has_key(shopping_car.product_id) else 1
        productsd = dict()
        for key in tmp:
            productsd[key]=get_product(key)

        self.render("car.html", products= tmp,productsd=productsd)

class BuyHistory(tornado.web.RequestHandler):
    '''
    购买历史
    '''
    def get(self, *args, **kwargs):
        user_id = self.get_secure_cookie("user_id")
        user_id = int(user_id)
        trans = get_buy_history(user_id)
        self.render("buy_history.html",
                    trans = trans)
        pass
    pass




