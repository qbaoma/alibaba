#coding=utf-8
__author__ = 'wxy'
#from dbUtil import MySQLUtil
from configparser import ConfigParser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
gconf=ConfigParser()
gconf.read('./global.ini')
def get_engin_str():
    '''
    获得初始化 engin 的字符串
    :return:
    '''
    #如果是 mysql 数据库
    if str(gconf.get('db','db'))==str('mysql'):
        user=str(gconf.get('db','user'))
        password=str(gconf.get('db','pass'))
        host=str(gconf.get('db','host'))
        port=str(gconf.get('db','port'))
        dbname=str(gconf.get('db','name'))
        return 'mysql+mysqldb://{0}:{1}@{2}:{3}/{4}'.format(
            user,password,host,port,dbname
        )
    return ''
#用于初始化 SqlAlchemy 的 engin
engin_str=get_engin_str()
engine_str=engin_str
engine = create_engine(engine_str)
Session = sessionmaker(bind=engine)

