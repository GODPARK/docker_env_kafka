## local kafka ( for dev )

## Port
* 9092: kafka Port
* 2181: zookeeper Port
* 8080: zookeeper admin Port

# project
* module: 구성 상 필요한 모듈 디렉토리
* test: 각종 테스트 코드를 위한 디렉토리 ex) kafka consumer , producer
* Dockerfile: 도커 이미지 구성을 위한 도커 파일
* kafka_setting.json: kafka 설정을 위한 설정 파일

# Module
* file_replace.py: 설정 파일 및 파일들의 내용 변경을 위한 python 스크립트
* start.sh: zookeeper, kafka start 를 위한 shell script

## docker build
`docker build -t kafka-local-env -f kafka/Dockerfile .`

## docker start
`docker run -d -p 8080:8080 -p 9092:9092 -p 2181:2181 --name kafka kafka-local-env`

## kafka topic 생성 방법
```
# docker 접속
$ docker exec -it kafka /bin/bash

$ test topic 생성
$ cd /usr/local/kafka/bin
$ /kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test
```

## docker image 내부에서 pub/sub 테스트
> console 터미널 창 두개 필요
```
# docker 접속
$ docker exec -it kafka /bin/bash

# 터미널 1
# test topic 에 대하여 pub
$ cd /usr/local/kafka/bin
$ /kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test

$ 터미널 2
# test topic 에 대하여 sub
$ cd /usr/local/kafka/bin
$ ./kafka-console-consumer.sh --topic test --bootstrap-server localhost:9092
```