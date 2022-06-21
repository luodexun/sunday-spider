import scrapy
from ..items import XiyouItem
import json
import re


class DahuaSpider(scrapy.Spider):
    name = 'dahua'
    allowed_domains = ['dhxy.cbg.163.com']
    start_urls = [
        'https://dhxy.cbg.163.com/cgi-bin/recommend.py?callback=jQuery3310928728289958515_1655781273943&act=recommd_by_role&search_type=role&count=15&client_type=h5&view_loc=equip_list&server_pay_type=1&order_by=&page=1&exter=www.baidu.com&page_session_id=01818435-5F55-1458-24BE-2403CB8C90FB&_=1655781273944']

    def parse(self, response):
        items = []
        res = re.search('\w+\((.+)\)', response.text)
        text = res.group(1)
        rs = json.loads(text)
        print(rs)
        return items
