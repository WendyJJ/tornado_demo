from kafka import KafkaProducer, KafkaConsumer
import time, json
producer = KafkaProducer(bootstrap_servers=["127.0.0.1:9092"])

# i = 20
# while True:
#     i += 1
#     msg = "producer1+%d" % i
#     print(msg)
#     producer.send('kafkatest', key=bytes(str(i).encode('utf-8')), value=msg.encode('utf-8'))
#     time.sleep(1)
#
# producer.close()

"""
    producer
"""
msg_dict = {
    "sleep_time": 10,
    "db_config": {
        "database": "test_1",
        "host": "xxxx",
        "user": "root",
        "password": "root"
    },
    "table": "msg",
    "msg": "Hello World"
}
msg = json.dumps(msg_dict)
producer.send('test_rhj', msg.encode('utf-8'), partition=0)
print(producer)
producer.close()


#
consumer = KafkaConsumer('test_rhj', bootstrap_servers=["127.0.0.1:9092"])
print(consumer,8888888888)
print(type(consumer))

dict = consumer.poll(500)
print(dict,77)
for key, value in dict.items():
    print(key)
    print()
    for record in value[:10]:
        print(record)
        print()
# for msg in consumer:
#     print(msg,9999999)

    # recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    # print(recv)
# if __name__ == '__main__':
#     consumer = KafkaConsumer('kafkatest', bootstrap_servers=['127.0.0.1:9092'])
#     for msg in consumer:
#         print(msg)