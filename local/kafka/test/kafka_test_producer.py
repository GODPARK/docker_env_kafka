from kafka import KafkaProducer
from json import dumps
import time

producer = KafkaProducer(acks=1, bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))

start = time.time()
for i in range(10):
    data = {'str' : 'result'+str(i)}
    producer.send('test', value=data)
    print("send: " + str(i))
    producer.flush()
print("elapsed :", time.time() - start)
