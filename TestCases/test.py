import unittest
from Utils.page import *
from Utils.tokeinfo import tokeninfo
class Totasks(unittest.TestCase,Helper):

    def test_bd(self):
        '''BD验证'''
        token = tokeninfo()
        url = 'http://webapi.loex.abc/exchange-web-api/v1/bd/verify'
        headers = {"Content-Type": "application/json;charset=UTF-8", "exchange-token": token}
        data = {'type':'Skype', 'content':'Skype'}
        r = self.post(url,data,headers)
        print(r.text)
        print(r.json()['msg'])
        self.assertEqual(r.json()['code'], '10003')
