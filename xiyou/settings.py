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
# USER_AGENT = 'xiyou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 8
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:

DEFAULT_REQUEST_HEADERS = {
    "accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "cbg-safe-code": "uY7Ae4gd",
    "cookie": "_ntes_nnid=b6b237ffc0efa18bf026b0637f13cb11,1635085552209; _ntes_nuid=b6b237ffc0efa18bf026b0637f13cb11; trace_session_id=0181B9C2-1E46-2EE9-6616-124330F0A051; fingerprint=3MyPwnGW0guUXVCJOR4Jh9AF; _flow_group=g3; _external_mark=www.baidu.com; NTES_YD_PASSPORT=WFTkE3ozB.JiIIxoxgkUK27LKMXhkSviPWlpb5ycZtFOHglxHydKU4yJcFb9O454ARpEm1eyp.aCwGdvyFedsaTZpB5sfO8AXXuz4OA4a34Uq6quJtYNe0n3C01NgsgKa5wqqQIX7uxkrcG5uSTLAlLxZTVYFec35t1qZ7eMaf56rqnl6Onv3gsK7go66zy5DhA0glAtLZgdZhTGOSESqpxCA; S_INFO=1656679022|0|0&60##|18006309740; P_INFO=18006309740|1656679022|1|cbg|00&99|null&null&null#sic&511700#10#0|&0||18006309740; urs_share_login_token=yd.9bf05514a3b44390a@163.com$93125b297558570bb722feb19108cd56; urs_share_login_token_h5=yd.9bf05514a3b44390a@163.com$93125b297558570bb722feb19108cd56; reco_sid=iGfeSegZqkEoFKJlCUo27d002-1BZuKXoEQQePV0; gdxidpyhxdE=H3Epo%5CeqeA3s5Onu1MLliYKWpRzAkqPBemmW3OzIZDVlHVcH%2B6Qw50lK5m2tgU%5Cn8NSEZYlhyHk6OtcON4z0aATB9IDtzusUeGj5w8TP9tQAt6dhtimhIdnhb3y5U768sdvrskDl%5CdnyCa%2BhTXUK%2FnvIBzz2fE1%2F4qptMO7iI%2BvuspVH%3A1656694395772; _9755xjdesxxd_=32; YD00000722197596%3AWM_NI=xUQl5%2FsVAGOs3oKZEmzefA5Zb9lySkzvUhkupzDUmeUosjEc%2BjNU7VXJHEZ4E7BEd7mQNvWwfL3GDY%2BTVCLhrymIi8x2LDaj9DdwhB0aqiES0twcTf7bJA8QqGzP0ylmcUU%3D; YD00000722197596%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed9ec5483bc98b7b141878e8fb3d54e879b8e86d54fb4f196d4d5548ca7abb3e92af0fea7c3b92abc8b9f8db825b18a8fa8ce79f1b185bbc867babbaaa2b852a2e7a49ad261baaa9b89ea7fb4a68cb6f06f97b1bd8bc869e9b682b6b65e9c9688a6d94087e98ea6e73daf8f8297d67da694fda8c753e98c9aa4cf64b2a7a3aaec34bcee84a5e462fb9cac98eb4af4bfbf8ac859f4acb984d76ef5be86a2bb5bb399b6b1b373b0b3adb6d837e2a3; YD00000722197596%3AWM_TID=G7Wc3bn8TuJEQFUREVfRAtrZmBDSzPQ2; is_log_active_stat=1; NTES_YD_SESS=PvP3PJF3lj98odG4C66UiPHnY1SDIf9K9.VbhcXicCxvtMe.tG1VzrGv0uTOwrHrojQg3sUGQy6iYvuLTJqzc1F0RW22KVJDLgNNCJN06sHFfRMnffZ4FDh5Qx5wflnVGSuq8Phko2r9O5FvaD2aCn92Q.kQuT8pK4bc.kLX9wfoq11tBtrpPUo5IHitSJwrhZ5mC6reaMi3THBq6_FG5qYgzcrTmwxvW; sid=v2.s.bxTkWZJSIEndtBTMwEPowWpkfrTwpUc0j77FHA8F6HYYYNu0; login_id=14241273-f9d3-11ec-a413-528df1699759",
    "referer": "https://dhxy.cbg.163.com/cgi/mweb/pl?server_pay_type=1&view_loc=equip_list",
    "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xiyou.middlewares.XiyouSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'xiyou.middlewares.XiyouDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'xiyou.pipelines.XiyouPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
