from kafka import KafkaProducer
from json import dumps
import time

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

start = time.time()
for i in range(10):
    data = {'str' : 'result'+str(i)}
    producer.send('test-topic', value=b'hello world').get(timeout=30)
    print("send: " + str(i))
    producer.flush()
print("elapsed :", time.time() - start)
