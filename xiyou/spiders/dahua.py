import scrapy
from scrapy import Request, FormRequest
import uuid
from urllib.parse import urlencode
import time
from ..items import XiyouItem
import json
import re


class DahuaSpider(scrapy.Spider):
    name = 'dahua'
    query = {
        "callback": "jQuery33108249397443390019_1656744548935",
        "act": "recommd_by_role",
        "search_type": "role",
        "count": 15,
        "client_type": "h5",
        "view_loc": "equip_list",
        "server_pay_type": 1,
        "order_by": "",
        "page": "1",
        "page_session_id": "0181BDAF-FC43-411F-DA29-59624499F094",
        "_": int(time.time() * 1000),
    }
    allowed_domains = ['dhxy.cbg.163.com']
    start_urls = ["https://dhxy.cbg.163.com/cgi-bin/recommend.py?{0}".format(urlencode(query))]

    def parse(self, response):
        items = []
        template = re.search('\w+\((.+)\)', response.text)
        res = json.loads(template.group(1))
        item = XiyouItem()
        lists = res['result']
        for element in lists:
            query = dict(
                serverid=str(element['serverid']),
                ordersn=element['game_ordersn'],
                view_loc="equip_list | tag_key:{'tag': 'user'}",
                exter="www.baidu.com",
                page_session_id=str(uuid.uuid4()).encode("utf-8")
            )
            print(query)
            yield scrapy.FormRequest(
                "https://dhxy.cbg.163.com/cgi/api/get_equip_detail",
                formdata=query,
                callback=self.detail,
                meta=item
            )
        pager = res['pager']
        if pager['cur_page'] < pager['total_pages']:
            query = {
                "callback": "jQuery33108249397443390019_1656744548935",
                "act": "recommd_by_role",
                "search_type": "role",
                "count": 15,
                "client_type": "h5",
                "view_loc": "equip_list",
                "server_pay_type": 1,
                "order_by": "",
                "page": pager['cur_page']+1,
                "page_session_id": "0181BDAF-FC43-411F-DA29-59624499F094",
                "_": int(time.time() * 1000),
            }
            yield Request("https://dhxy.cbg.163.com/cgi-bin/recommend.py?{0}".format(urlencode(query)), callback=self.parse)

    def detail(self, response):
        item = response.meta
        result = json.loads(response.body)
        if result["status"] == 1:
            item['status'] = result["status"]
            item['statusCode'] = result["status_code"]
            item['createTime'] = result["server_now_time"]
            item['updateTime'] = result["server_now_time"]
            element = result['equip']
            if element is not None:
                item['sellerRoleid'] = element["seller_roleid"]
                item['cbgUrl'] = element["equip_detail_url"]
                item['level'] = element["level_desc"]
                item['sellerName'] = element["seller_name"]
                item['statusDesc'] = element["status_desc"]
                item['serverId'] = element["serverid"]
                item['serverName'] = element["server_name"]
                item['gameChannel'] = element["game_channel"]
                item['price'] = element["price"] / 100
                item['areaName'] = element["area_name"]
                item['playName'] = element["format_equip_name"]
                item['umupShort'] = element["desc_sumup_short"]
                desc = json.loads(element['equip_desc'])
                basic = desc["Basic"]
                if basic is not None:
                    item['xiaYu'] = basic["CbgXianYuFzn"]
                    item['silver'] = basic["CbgYinLiangFzn"]
                    item['wuXingLevel'] = basic["WuXingLevel"]
                    item['hp'] = basic["HpMax"]
                    item['mp'] = basic["HpMax"]
                    item['ap'] = basic["Atk"]
                    item['sp'] = basic["Speed"]
                    item['factionLevel'] = basic["OrgShouHu"]
                    item['tianYanLevel'] = basic["OrgTianFuTotalPoint"]
                    item['fire'] = basic['WuXingInfo']["Fire"]
                    item['soil'] = basic['WuXingInfo']["Soil"]
                    item['water'] = basic['WuXingInfo']["Water"]
                    item['wood'] = basic['WuXingInfo']["Wood"]
                    item['gold'] = basic['WuXingInfo']["Gold"]
                acsry = desc['SuitInfo']
                if acsry and acsry is not None:
                    item['suitLevel'] = acsry["Level"]
                    item['suitName'] = acsry["Name"]
                else:
                    item['suitLevel'] = 0
                    item['suitName'] = "暂无数据"
        yield item
