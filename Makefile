OPENCV_VERSION=4.2.0

build:
	docker build -f Dockerfile philiplinden/opencv:${OPENCV_VERSION} .

pull:
	docker pull philiplinden/opencv:${OPENCV_VERSION}

push:
	docker push philiplinden/opencv:${OPENCV_VERSION}
