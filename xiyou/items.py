# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiyouItem(scrapy.Item):
    # define the fields for your item here like:
    sellerRoleid = scrapy.Field()
    level = scrapy.Field()
    sellerName = scrapy.Field()
    playName = scrapy.Field()
    areaName = scrapy.Field()
    serverId = scrapy.Field()
    serverName = scrapy.Field()
    price = scrapy.Field()
    statusDesc = scrapy.Field()
    cbgUrl = scrapy.Field()
    gameChannel = scrapy.Field()
    umupShort = scrapy.Field()
    xiaYu = scrapy.Field()
    silver = scrapy.Field()
    hp = scrapy.Field()
    mp = scrapy.Field()
    ap = scrapy.Field()
    sp = scrapy.Field()
    factionLevel = scrapy.Field()
    tianYanLevel = scrapy.Field()
    wuXingLevel = scrapy.Field()
    fire = scrapy.Field()
    soil = scrapy.Field()
    water = scrapy.Field()
    wood = scrapy.Field()
    gold = scrapy.Field()
    suitLevel = scrapy.Field()
    suitName = scrapy.Field()
    status = scrapy.Field()
    statusCode = scrapy.Field()
    createTime = scrapy.Field()
    updateTime = scrapy.Field()
    pass
