# -*- coding: utf-8 -*-
import json
import requests

'''
====== 本程序用于实现对于饿了么网站的数据采集 ======
    核心:
        根据饿了么的对外接口和reqeusrs的调用。
    author:
        handsomer
'''
class elemeSpider():
    '''
            第一步:
                根据传参地址获取周边的商铺信息
            返回值中包含了商铺的信息：
                组成商铺详细url关键信息, geohash
    '''
    def GetShopList(self):
        location = "望京SOHO"
        start_urls = ("https://www.ele.me/restapi/v2/pois?extras%5B%5D=count&geohash=wx4g0bmjetr7&keyword={}&limit=20&type=nearby".format(location),)
        ret_value = requests.get(url = start_urls[0])
        self.parse_shoplist(ret_value.text)

    '''
        第二步:
            遍历所有商铺，获得单个商铺的链接
            返回值中包含了商铺的信息
    '''
    def parse_shoplist(self, ret_text):
        json_data = json.loads(ret_text)
        print(type(json_data))
        elem = json_data[0]
        for i in range(1,50):
            offset = i *24
        offset = 24
        shop_url = "https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash={}&latitude={}&limit=24&longitude={}&offset={}&terminal=web".format(elem["geohash"],elem["latitude"],elem["longitude"],offset)
        ret_value = requests.get(url = shop_url)
        ret_text = ret_value.text
        json_data = json.loads(ret_text)
        shop_detail = "https://www.ele.me/restapi/shopping/v2/menu?restaurant_id="
        for elem in json_data:
            target_url = shop_detail + elem["scheme"].split('=')[1]
            self.parse_shop_food(url=target_url)

    '''
        第三步:
            解析单个商铺的销售情况（根据各个单品的销售情况，计算该商铺的收入情况）
    '''
    def parse_shop_food(self, ):
        pass


m_obj = elemeSpider()
m_obj.GetShopList()