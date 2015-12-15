#coding=utf-8
__author__ = 'wxy'

import unittest
from db.dbUtil import save_new_user,check_user,save_product
from db.dbUtil import get_all_products

class TestDb(unittest.TestCase):
    '''
    db 部分的单元测试
    '''
    def test_save_new_user(self):
        try:
            save_new_user('18810541263','0603')
        except:
            pass

    def test_check_user(self):
        res = check_user('1881054126','wang')
        self.assertEqual(res,False)
        res = check_user('18810541263','0603')
        self.assertEqual(res,True)
        res = check_user('18810541263','11')
        self.assertEqual(res,False)

    def test_save_product(self):
        res = save_product(12,'mestory','http://www.baidu.com')
        self.assertEqual(res,True)

    def test_get_all_products(self):
        products = get_all_products()





