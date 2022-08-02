
KAFKA1_PATH=/usr/local/kafka1
KAFKA2_PATH=/usr/local/kafka2
DOCKER_CONTAINER=kafka-cluster
DOCKER_IMAGE_NAME=kafka-cluster-loal
PORT1=9092
PORT2=9093

install: clean build run

build:
	-docker build -t $(DOCKER_IMAGE_NAME) .

clean:
	-docker stop $(DOCKER_CONTAINER)
	-docker rm $(DOCKER_CONTAINER)

run:
	-docker run -d -p $(PORT1):$(PORT1) -p $(PORT2):$(PORT2) --name $(DOCKER_CONTAINER) $(DOCKER_IMAGE_NAME)

fgrun:
	-docker run -it -p $(PORT1):$(PORT1) -p $(PORT2):$(PORT2) --name $(DOCKER_CONTAINER) $(DOCKER_IMAGE_NAME)

ssh:
	-docker exec -it $(DOCKER_CONTAINER) /bin/bash

allClean:
	-docker image prune -f
	-docker container prune -f
