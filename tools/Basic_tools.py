import pymysql
from DBUtils.PooledDB import PooledDB
import logging
import redis

import sys
sys.path.append("../..")

from tools.config_tools import *



class mysql_connection(object):
    def __init__(self):
        """

        :param host:
        :param user:
        :param passwd:
        :param db:
        :param port:
        :param charset:
        ----------------- 以下参数选填 -----------------
        :param mincached: # 连接池里的最少连接数
        :param maxcached: # 最大的空闲连接数，如果空闲连接数大于这个数，pool会关闭空闲连接
        :param maxshared: # 当连接数达到这个数，新请求的连接会分享已经分配出去的连接
        :param maxconnections: # 最大的连接数，
        :param blocking: # 当连接数达到最大的连接数时，在请求连接的时候，如果这个值是True，请求连接的程序会一直等待，
        直到当前连接数小于最大连接数，如果这个值是False，会报错
        """
        self.host = sql_host
        self.user = sql_user
        self.passwd = sql_passwd
        self.db = sql_db
        self.port = sql_port
        self.charset = sql_charset
        self.mincached = sql_mincached
        self.maxcached = sql_maxcached
        self.maxshared = sql_maxshared
        self.maxconnections = sql_maxconnections
        self.blocking = sql_blocking
        self.conn_pool = PooledDB(pymysql,mincached=sql_mincached,maxcached=sql_maxcached,maxshared=sql_maxshared,
                                maxconnections=sql_maxconnections,blocking=sql_blocking,host=sql_host,
                                user=sql_user,passwd=sql_passwd,db=sql_db,port=sql_port,charset=sql_charset).connection()

    def mysql_tools(self,sql,state=True):
        """
        :param conn: 报错 pymysql.err.InterfaceError: (0, '')
        :param sql: 传入完整原生sql
        :param state: 选填，当此值为false时使用数据库连接池
        :return: 当次查询结果
        """
        try:
            if state == True:
                conn = pymysql.connect(host= self.host, user=self.user,passwd=self.passwd,db=self.db)
            else:
                conn = self.conn_pool
            # conn.ping(reconnect=True)
            cursor = conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            logging.info("sql success")
            return data
        except:
            logging.exception('sql Error! sql = '+str(sql))
            return False
        finally:
            conn.commit()
            cursor.close()
            conn.close()


class redis_connection():

    def __init__(self):
        """
        :param host:
        :param port:
        :param decode_responses:
        :param db:
        :param password:
        :param state: 此字段为True时使用redis标准链接，否则使用连接池
        """
        self.host = redis_host
        self.port = redis_port
        self.decode_responses = redis_decode_responses
        self.db = redis_db
        self.password=redis_password
        self.state = redis_state
        self.conn = redis.StrictRedis(host=redis_host, port=redis_port,db=redis_db)
        self.conn_pool = redis.StrictRedis(connection_pool=redis.ConnectionPool(host=redis_host,
                                                                                password=redis_password,
                                                                                port=redis_port,
                                                                                decode_responses=redis_decode_responses,
                                                                                db=redis_db))
    def get(self,key):
        try:
            if self.state:
                return self.conn.get(key)
            else:
                return self.conn_pool.get(key)
        except Exception as e:
            return e

    def set(self,key,val,period=None):
        try:
            if self.state:
                self.conn.set(key, val)
                if period:
                    self.conn.expire(key,period)
                return True
            else:
                self.conn_pool.set(key, val)
                if period:
                    self.conn.expire(key,period)
                return True
        except Exception as e:
            return e


if __name__ == '__main__':
    a = redis_connection()
    print(a.set('test','test1111'))