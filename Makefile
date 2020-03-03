DOCKER_TAG = latest

build:
	docker build -f Dockerfile philiplinden/enhance:${DOCKER_TAG} .

pull:
	docker pull philiplinden/enhance:${DOCKER_TAG}

push:
	docker push philiplinden/enhance:${DOCKER_TAG}
