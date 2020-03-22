import os
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line
from app.urls import *

# 定义默认启动的端口port为8000
define('port', default=8000, type=int)



if __name__ == '__main__':
    #解析启动命令， 启动命令为： python xxx.py --port=端口号
    parse_command_line()
    # 启动
    app = make_app()
    # 监听端口
    app.listen(options.port)
    # 监听启动的IO实例
    tornado.ioloop.IOLoop.current().start()