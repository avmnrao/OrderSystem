# Producer Section
# import packages

from time import sleep
from json import dumps
from kafka import KafkaProducer

# initialize a new Kafka producer

producer = KafkaProducer(bootstrap_servers=['avmnrao:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
orders_RDD = sc.textFile("/user/avmnrao/hadoop/python/orders")
for e in orders_RDD():
    data = {'record_id': e}
    producer.send('orders', value=data)
    sleep(5)
    
# Consumer Section
# Packages
from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'orders',
     bootstrap_servers=['avmnrao:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='orders-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
