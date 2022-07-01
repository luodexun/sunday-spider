import scrapy
from scrapy import Request

from ..items import XiyouItem
import json
import re


class DahuaSpider(scrapy.Spider):
    name = 'dahua'
    allowed_domains = ['dhxy.cbg.163.com']
    start_urls = [
        'https://dhxy.cbg.163.com/cgi-bin/recommend.py?callback=jQuery33101968190463245152_1656036301854&act=recommd_by_role&search_type=role&count=15&client_type=h5&view_loc=equip_list&server_pay_type=1&order_by=&page=1&page_session_id=0181936C-322F-2CF3-74EE-D8065B36DCF4&_=1656036301855']

    def parse(self, response):
        items = []
        res = re.search('\w+\((.+)\)', response.text)
        text = res.group(1)
        rs = json.loads(text)
        item = XiyouItem()
        lists = rs['result']
        for element in lists:
            item['price'] = element["price"]
            yield Request(url='https://dhxy.cbg.163.com/cgi/api/get_equip_detail', method='post', callback=self.detail,meta = dict(item))
        yield Request('https://dhxy.cbg.163.com/cgi-bin/recommend.py')

    def detail(self, response):
        item = response.meta
        element = response['equip']
        item['sellerRoleid'] = element["seller_roleid"]
        item['level'] = element["level_desc"]
        item['sellerName'] = element["seller_name"]
        item['playName'] = element["format_equip_name"]
        item['areaName'] = element["area_name"]
        item['serverId'] = element["serverId"]
        item['serverName'] = element["server_name"]
        item['statusDesc'] = element["status_desc"]
        item['cbgUrl'] = element["equip_detail_url"]
        item['gameChannel'] = element["game_channel"]
        item['umupShort'] = element["desc_sumup_short"]
        desc = json.loads(['equip_desc'])
        item['xiaYu'] = desc["XiaYi"]
        item['silver'] = desc[""]
        item['hp'] = desc["HpMax"]
        item['mp'] = desc["MpMax"]
        item['ap'] = desc[""]
        item['sp'] = desc[""]
        item['factionLevel'] = desc[""]
        item['tianYanLevel'] = desc[""]
        item['wuXingLevel'] = desc["WuXingLevel"]
        item['fire'] = desc['WuXingInfo']["Fire"]
        item['soil'] = desc['WuXingInfo']["Sater"]
        item['water'] = desc['WuXingInfo']["Water"]
        item['wood'] = desc['WuXingInfo']["Wood"]
        item['gold'] = desc['WuXingInfo']["Gold"]
        item['suitLevel'] = element[""]
        item['suitName'] = desc[""]
        item['status'] = element["status"]
        item['statusCode'] = element[""]
        item['createTime'] = element[""]
        item['updateTime'] = element[""]
        yield item
