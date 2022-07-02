# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class XiyouPipeline:
    def __init__(self):
        self.ids_seen = set()  # 初始化一个无序不重复集和ids_seen
        self.conn = pymysql.connect(host='101.43.40.89', user='root', password='sqlapp2020xx', database='dhxy',
                                    charset='utf8')

    def process_item(self, item, spider):
        try:
            self.ids_seen.add(item['sellerRoleid'])
            cursor = self.conn.cursor()
            sql = 'insert ignore into cbg_role_info (sellerRoleid,level,sellerName,playName,areaName,serverId,serverName,price,statusDesc,cbgUrl,gameChannel,umupShort,xiaYu,silver,hp,mp,ap,sp,factionLevel,tianYanLevel,wuXingLevel,fire,soil,water,wood,gold,suitLevel,suitName,status,statusCode,createTime,updateTime) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            data = [item['sellerRoleid'], item['level'], item['sellerName'], item['playName'], item['areaName'],
                    item['serverId'], item['serverName'], item['price'], item['statusDesc'], item['cbgUrl'],
                    item['gameChannel'], item['umupShort'], item['xiaYu'], item['silver'], item['hp'], item['mp'],
                    item['ap'], item['sp'], item['factionLevel'], item['tianYanLevel'], item['wuXingLevel'],
                    item['fire'], item['soil'], item['water'], item['wood'], item['gold'], item['suitLevel'],
                    item['suitName'], item['status'], item['statusCode'], item['createTime'], item['updateTime']]
            res = cursor.execute(sql, data)
            print(res)
            self.conn.commit()
            cursor.close()
            return item
        except Exception as e:
            print(e)
