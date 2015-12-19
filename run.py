#coding=utf-8
__author__ = 'wxy'
import os.path

import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import define,options
define("port",default=8000,help="run on the given port",type=int)

from taobao.index import IndexHandler,LoginHandler,RegisterHandler
from taobao.index import RegistFailHandler
from taobao.shoping import WelcomeHandler,LogoutHandler,ProductHandler
from paypal.paypal import CreatePayPayl,PayPayl,AllPayPayl
from taobao.shoping import AddShoppingCart,Car
from taobao.shoping import BuyProduct,BuyHistory

#all setting including url pattern

settings ={
    #"xsrf_cookies":True,
    "cookie_secret":"tzxSX5owRf+Fpeboi7LGVgVoBcIJkUmTnM6UD9Q4TCM="
}
app = tornado.web.Application(
    handlers=[
        (r'/',WelcomeHandler),
        (r'/login',IndexHandler),
        (r'/login_form',LoginHandler),
        (r'/regist_form',RegisterHandler),
        (r'/regist',RegisterHandler),
        (r'/regist_fail',RegistFailHandler),
        (r'/logout',LogoutHandler),
        (r'/product',ProductHandler),
        (r'/products',ProductHandler),
        (r'/product/([0-9]+)',ProductHandler),
        (r'/createPayPayl',CreatePayPayl),
        (r'/account/([0-9]+)',PayPayl),
        (r'/allpaypal',AllPayPayl),
        (r'/addcar',AddShoppingCart),
        (r'/car',Car),
        (r'/buy',BuyProduct),
        (r'/buy_history',BuyHistory)
    ],
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(
        os.path.dirname(__file__),"static"
    ),
    debug=True,**settings
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()