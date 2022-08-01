KAFKA_PATH=/usr/local/kafka
KAFKA_BIN_PATH=${KAFKA_PATH}/bin
KAFKA_CONFIG_PATH=${KAFKA_PATH}/config

MY_IP=`ifconfig eth0 | grep 'inet' | awk '{print$2}'`
BORKER_PORT=9092
TEST_TOPIC=test-topic