"""
@author: wjj
@time: 2019/4/10
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 回调地址配置
IP_NAME = '*******************'
DOMAIN_NAME = '*******************'


# mysql server 配置
sql_host = '*******************'
sql_user = '*******************'
sql_passwd = '*******************'
sql_db = '*******************'
sql_port=3306
sql_charset='utf8'
sql_mincached=1
sql_maxcached=5
sql_maxshared=1000
sql_maxconnections=2000
sql_blocking=True



# redis server 配置
redis_host='*******************'
redis_port=6379
redis_db=0
redis_decode_responses=True
redis_password=None
redis_state=False

# AWS配置W
AWS_ACCESS_KEY_ID = '*******************'
AWS_SECRET_ACCESS_KEY = '*******************'

