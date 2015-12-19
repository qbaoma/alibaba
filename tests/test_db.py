#coding=utf-8
__author__ = 'wxy'

import unittest
from db.dbUtil import save_new_user,check_user,save_product
from db.dbUtil import get_all_products,get_user_blances
from db.dbUtil import add_paypal_account,user_pay,add_car
class TestDb(unittest.TestCase):
    '''
    db 部分的单元测试
    '''
    tmp = 0
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

    def test_add_paypal_account(self):
        '''
        测试添加支付宝账户，所有金额都会添加到
        User.id == 1 的账户
        :return:
        '''
        accountId = add_paypal_account(1,10)
        self.assertTrue(accountId)
        self.tmp = accountId

    def test_get_user_balances(self):
        '''
        用上面生成的支付宝账户执行测试
        :return:
        '''
        user_balances = get_user_blances(1)
        for user_balance in user_balances:
            self.assertEqual(user_balance.balance,10)

    def test_zuser_pay(self):
        '''
        测试付款
        :return:
        '''
        res = user_pay(1,1,1)
        self.assertTrue(res)
        res = user_pay(10,1,10)
        self.assertFalse(res)

    def test_add_car(self):
        '''
        测试添加购物车
        :return:
        '''
        res = add_car(1,1,8)
        self.assertEqual(res,0)






