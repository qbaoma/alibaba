#coding=utf-8
__author__ = 'wxy'

from sqlalchemy import Column,create_engine
from sqlalchemy import Integer,String,DateTime,BigInteger,Boolean
from sqlalchemy import Text,ForeignKey
from sqlalchemy.orm import relationship,backref,sessionmaker
from . import Session,engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

#淘宝的用户
class User(Base):

    __tablename__="user"

    id = Column(Integer,primary_key=True,unique=True)
    account = Column(String(40),nullable=False,unique=True)
    passw = Column(String(40),nullable=False)
    registTime = Column(DateTime,nullable=False)

#支付宝账户
class PaypalAccount(Base):

    __tablename__="paypalaccount"

    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    balance = Column(Integer,nullable=False,default=0)

#淘宝商品
class Product(Base):

    __tablename__="product"

    id = Column(Integer,primary_key=True)
    price = Column(Integer,nullable=False,default=0)
    desc = Column(Text,nullable=True)
    picture = Column(String(40),nullable=True)

#交易记录
class Transaction(Base):

    __tablename__="transaction"

    id = Column(Integer,primary_key=True)
    buyer_id = Column(Integer,ForeignKey('user.id'))
    product_id = Column(Integer,ForeignKey('product.id'))
    tra_time = Column(DateTime,nullable=False)

    product = relationship(
        "Product",backref = backref('transactions',order_by=id)
    )
    user = relationship(
        "User",backref = backref('transactions',order_by=id)
    )

#购物车
class ShoppingCart(Base):

    __tablename__="shopping_cart"

    id = Column(Integer,primary_key=True)
    buyer_id = Column(Integer,ForeignKey('user.id'))
    product_id = Column(Integer,ForeignKey('product.id'))
    add_time = Column(DateTime,nullable=False)

    user = relationship(
        "User",backref = backref('shopping_carts',order_by=id)
    )

def create_db():
    '''
    创建数据库
    :return:
    '''
    Base.metadata.create_all(engine)
    session = Session()
    session.commit()

if __name__=="__main__":
    create_db()