import tornado.web
from app.models import *
from tornado.httpclient import AsyncHTTPClient
from tornado.web import RequestHandler
import json
import pymysql
from datetime import datetime, timedelta
from tools.DynamoDB_tools import *

class InitDbHandler(RequestHandler):

    async def get(self):
        # 将模型映射到数据库中
        init_db()
        self.write("创建表成功")

class PostHandler(RequestHandler):
    """
    POST请求方法实例
    """
    async def post(self):
        try:
            face_img = self.get_argument("face_img")
            username = self.get_argument("username")
            realname = self.get_argument("realname")
            print("face_img==", face_img, "username==",username, "realname==",realname)
            if all([face_img, username, realname]):

                table_name = "user_info"
                data = save_data('record_info', data={
                        'uid': "999999999999999999999",
                        'rank': 'perfect',
                        'c_id': str(777777777777777777),
                        'personal_state': "2"
                    })
                sql = save_data(table_name, data)
                self.write(json.dumps({"msg": "success"}).encode())
                # 设置响应状态码
                self.set_status(200)
                # 设置cookie
                self.set_cookie('token', '123456')
            else:
                error = "请填写完整信息"
                self.write(json.dumps(error).encode())
        except Exception as e:
            print(e)
            self.write(json.dumps("error").encode())

    def delete(self):
        self.write("delect: 只负责删除")

    def patch(self):
        self.write("patch：修改部分属性")


    def put(self):

        self.write("put： 修改全部数据")
class GetHandler(RequestHandler):
    """
    GET 请求方法实例
    """
    async def get(self):
        name = self.get_argument("name")
        print("name====", name)
        self.write("HELLO WORLD!!!!!!!!!!!")
        # 设置响应状态码
        self.set_status(200)
        # 设置cookie, 其中的expire参数表示过期时间， 到了过期时间，自动删除
        # self.set_cookie('token', '123456', expires_days=1)
        # out_time = datetime.now() + timedelta(days=1)
        # self.set_cookie('token123', 'efreeere', expires=out_time)

        # 删除cookie中的token键值对
        # self.clear_cookie('token')
        self.clear_all_cookies()
        # 跳转
        self.redirect('/')



class EntryHandler(RequestHandler):

    def initialize(self):

        # 实现功能是访问数据库，查询出学生的所有信息
        self.conn = pymysql.Connection(host='127.0.0.1', password = '123456',
                                       database = 'mydb', user = 'root', port =3306)

        self.cursor = self.conn.cursor()
        print("initialize")


    def prepare(self):
        print('prepare')


    def get(self):
        print('get')
        sql = 'select * from stu;'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)
        self.write('查询数据')

    def post(self):
        pass

    def on_finish(self):
        # 最后执行的方法
        print('on_finish')
        self.conn.close()

