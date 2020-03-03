FROM philiplinden/opencv:latest

WORKDIR /app

# install python dependencies
RUN pip3 install \
	click
