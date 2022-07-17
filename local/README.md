## local kafka ( for dev )

## Port
* 9092: kafka Port
* 2181: zookeeper Port
* 8080: zookeeper admin Port

# Module
* file_replace.py: 설정 파일 및 파일들의 내용 변경을 위한 python 스크립트
* start.sh: zookeeper, kafka start 를 위한 shell script

## docker build
`docker build -t kafka-local-env -f kafka/Dockerfile .`

## docker start
`docker run -d -p 8080:8080 -p 9092:9092 -p 2181:2181 kafka-local-env`