FROM ubuntu:focal

EXPOSE 9092
EXPOSE 8080
EXPOSE 2181

ENV KAFKA_SCALA=2.12 \
    KAFKA_VERSION=3.2.0 \
    INSTALL_JDK_VERSION=11-jre \
    WORK_PATH=/root/temp \
    SERVICE_PATH=/usr/local \
    KAFKA_DATA=/data/kafka
    
ENV KAFKA_FULL_VERSION=${KAFKA_SCALA}-${KAFKA_VERSION} \
    ZOO_BIN=${SERVICE_PATH}/bin\
    KAFKA_BIN=${SERVICE_PATH}/bin\
    ZOO_CONF=${SERVICE_PATH}/config\
    KAFKA_CONF=${SERVICE_PATH}/config

RUN apt-get upgrade -y
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install wget -y
RUN apt-get install net-tools -y && apt-get install vim -y
RUN apt-get install openjdk-${INSTALL_JDK_VERSION} -y

RUN mkdir ${WORK_PATH}

RUN cd ${WORK_PATH} && wget https://dlcdn.apache.org/kafka/${KAFKA_VERSION}/kafka_${KAFKA_FULL_VERSION}.tgz

RUN cd ${WORK_PATH} && tar -zxvf kafka_${KAFKA_FULL_VERSION}.tgz

RUN mv ${WORK_PATH}/kafka_${KAFKA_FULL_VERSION} ${SERVICE_PATH}/kafka

COPY ./module/* ${WORK_PATH}/
COPY ./kafka_setting.json ${WORK_PATH}/
RUN chmod 777 ${WORK_PATH}/start.sh

RUN mkdir /data
RUN mkdir ${KAFKA_DATA}
RUN mkdir /data/zookeeper
RUN mkdir /data/log

RUN python3 ${WORK_PATH}/file_replace.py --config ${WORK_PATH}/kafka_setting.json

CMD ["/root/temp/start.sh"]