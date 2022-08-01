
KAFKA_PATH=/usr/local/kafka
DOCKER_CONTAINER=kafka
DOCKER_IMAGE_NAME=kafka-loal
PORT=9092

install: clean build run

build:
	-docker build -t $(DOCKER_IMAGE_NAME) .

clean:
	-docker stop $(DOCKER_CONTAINER)
	-docker rm $(DOCKER_CONTAINER)

run:
	-docker run -d -p $(PORT):$(PORT) --name $(DOCKER_CONTAINER) $(DOCKER_IMAGE_NAME)

ssh:
	-docker exec -it $(DOCKER_CONTAINER) /bin/bash

allClean:
	-docker image prune -f
	-docker container prune -f

producer:
	python3 ./test/kafka_test_producer.py

consumer:
	python3 ./test/kafka_test_consumer.py