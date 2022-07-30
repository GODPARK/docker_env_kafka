#!/bin/bash

KAFKA_PATH=/usr/local/kafka
KAFKA_BIN_PATH=${KAFKA_PATH}/bin
KAFKA_CONFIG_PATH=${KAFKA_PATH}/config

echo "alias cd_kafka='cd ${KAFKA_PATH}'" >> ~/.bash_profile
echo "alias cd_work='cd /root/temp'" >> ~/.bash_profile
source ~/.bash_profile


${KAFKA_BIN_PATH}/zookeeper-server-start.sh ${KAFKA_CONFIG_PATH}/zookeeper.properties &
sleep 7s
${KAFKA_BIN_PATH}/kafka-server-start.sh ${KAFKA_CONFIG_PATH}/server.properties

