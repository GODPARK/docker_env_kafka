#!/bin/bash

KAFKA1_PATH=/usr/local/kafka1
KAFKA1_BIN_PATH=${KAFKA1_PATH}/bin
KAFKA1_CONFIG_PATH=${KAFKA1_PATH}/config

KAFKA2_PATH=/usr/local/kafka2
KAFKA2_BIN_PATH=${KAFKA2_PATH}/bin
KAFKA2_CONFIG_PATH=${KAFKA2_PATH}/config


${KAFKA1_BIN_PATH}/zookeeper-server-start.sh ${KAFKA1_CONFIG_PATH}/zookeeper.properties &

sleep 7s

${KAFKA1_BIN_PATH}/kafka-server-start.sh ${KAFKA1_CONFIG_PATH}/server.properties &

sleep 7s

${KAFKA2_BIN_PATH}/kafka-server-start.sh ${KAFKA2_CONFIG_PATH}/server.properties