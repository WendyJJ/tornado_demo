# from tornado.httpclient import HTTPClient
# from tornado.httpclient import AsyncHTTPClient
# import json
# from tornado import gen
#
#
#
# def synchronous_fetch(url):
#     http_client = HTTPClient()
#     response = http_client.fetch(url)
#     print(response)
#     return response.body
#
#
#
# async def asynchronous_fetch(url):
#     http_client = AsyncHTTPClient()
#     respose = await http_client.fetch(url)
#     return respose.body
#
#
#
#
# @gen.coroutine
# def async_fetch_gen(url):
#     http_client = AsyncHTTPClient()
#     response = yield http_client.fetch(url)
#     raise gen.Return(response.body)
#
#
#
# a = synchronous_fetch("http://www.baidu.com")
# b = asynchronous_fetch("http://www.baidu.com")
# print(type(a))
# print(a)
# print("======================")
# print(type(b))
# print(b)


# kafka-server-start.sh config/server.properties
# kafka-server-start.sh config/server.properties


from kafka import KafkaProducer
from pykafka import KafkaClient
producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
print(producer)
# #此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]
for i in range(3):
     msg = i
     print(msg)
     producer.send('test', m)
producer.close()


#
# client = KafkaClient(hosts="127.0.0.1:2180")
# for topic in client.topics:
#     print(topic)

