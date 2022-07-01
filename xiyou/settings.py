# Scrapy settings for xiyou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xiyou'

SPIDER_MODULES = ['xiyou.spiders']
NEWSPIDER_MODULE = 'xiyou.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xiyou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:

DEFAULT_REQUEST_HEADERS = {
    'Host': 'dhxy.cbg.163.com',
        'sec-ch-ua': ' Not A;Brand;v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'accept':'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'cbg-safe-code': '45ruD7R0',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': "macOS",
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://dhxy.cbg.163.com/cgi/mweb/pl?server_pay_type=1&view_loc=equip_list',
        'accept-encoding': "gzip, deflate, br",
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cookie': '_ntes_nnid=822c3b34d4bff19239dbd18946415de1,1629528567510; _ntes_nuid=822c3b34d4bff19239dbd18946415de1; fingerprint=hs8K6IlJhnWojeIqTDM8tFDj; _flow_group=g5; P_INFO=18876912016|1655102900|1|cbg|00&99|null&null&null#sic&510100#10#0|&0|null|18876912016; trace_session_id=01818038-C4AD-C0AC-9E90-3A5A78D305EE; _external_mark=www.baidu.com; urs_share_login_token=yd.74b14ba2ab1f42b18@163.com$fac907033765687486ace79a5ee3ffdb; urs_share_login_token_h5=yd.74b14ba2ab1f42b18@163.com$fac907033765687486ace79a5ee3ffdb; reco_sid=ItC66DhtseP2T5XUKNPFIy4qDv_q8LaRHG0UE7cI; NTES_YD_SESS=XhPIzJkdJQyrRzynRI8AYqfE_8OIL75S7jSTCTusyQnDHglxHydKU41s0Ff8rfoM.M89TONeBK3Xw3MIXJn9ud374UeNo9WQ30502iax1gbOA_JHrADa31GCZ02L52Oxzzm.9P.g65LixyG6QxndMy4hRJ2OXQezH1bvmgMR8MHGJydN1pHcJbh_ngiR0QMPchBs5m1XXOvcJBYJ_0018VHaJ9b8PLTDq; timing_user_id=time_4cNH0gwi1L; _nietop_foot=%u5927%u8BDD%u897F%u6E38%u624B%u6E38%7Cdhxy.163.com; is_log_active_stat=1; sid=v2.s.F_oPnXW_IfkFR4vO_OL4j0755vAc5gggJXqMpL5qjCPFtDYL; login_id=c5acfaf8-f360-11ec-9403-e7d5dbc4db4c'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'xiyou.middlewares.XiyouSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'xiyou.middlewares.XiyouDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'xiyou.pipelines.XiyouPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
