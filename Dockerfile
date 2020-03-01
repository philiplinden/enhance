FROM python:3.6-alpine

WORKDIR /usr/src/

# update apk index
RUN apk update

# install developer tools
RUN apk add \
	bash \
	build-base \
	ca-certificates \
	clang-dev \
	clang \
	cmake \
	coreutils \
	curl \ 
	gcc \
	g++ \
	git \
	gettext \
	libwebp-dev \
	linux-headers \
	make \
	musl \
	openssl \
	python3-dev \
	unzip \
	zlib-dev

# install image, video and I/O libraries
RUN apk add \
	ffmpeg-dev \
	ffmpeg-libs \
	lcms2-dev \
	libavc1394-dev \
	libc-dev \
	libffi-dev \
	libjpeg-turbo-dev \
	libpng-dev \
	libressl-dev \
	openjpeg-dev \
	tiff-dev

# install python dependencies
RUN pip3 install \
	numpy

# OpenCV Version
ENV OPENCV_VERSION 4.2.0

RUN mkdir /usr/src/opencv-tmp

# download and extract OpenCV core
RUN wget -O /usr/src/opencv-tmp/opencv.zip https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip \
	&& unzip /usr/src/opencv-tmp/opencv.zip \
	&& mv opencv-${OPENCV_VERSION} /usr/src/opencv

# download and extract OpenCV contrib
RUN wget -O /usr/src/opencv-tmp/opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/${OPENCV_VERSION}.zip \
	&& unzip /usr/src/opencv-tmp/opencv_contrib.zip \
	&& mv opencv_contrib-${OPENCV_VERSION} /usr/src/opencv_contrib

WORKDIR /usr/src/opencv/build

# configure compilation options
RUN cmake \
	-D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_C_COMPILER=/usr/bin/clang \
    -D CMAKE_CXX_COMPILER=/usr/bin/clang++ \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D OPENCV_EXTRA_MODULES_PATH=/usr/src/opencv_contrib/modules \
	-D PYTHON3_LIBRARY=`python -c 'import subprocess ; import sys ; s = subprocess.check_output("python-config --configdir", shell=True).decode("utf-8").strip() ; (M, m) = sys.version_info[:2] ; print("{}/libpython{}.{}.dylib".format(s, M, m))'` \
	-D PYTHON3_INCLUDE_DIR=`python -c 'import distutils.sysconfig as s; print(s.get_python_inc())'` \
	-D PYTHON3_EXECUTABLE=/usr/local/bin/python3 \
	-D BUILD_opencv_python2=OFF \
	-D BUILD_opencv_python3=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D BUILD_EXAMPLES=ON \
	..

# compile (with 4 threads)
RUN make -j4

# install
RUN make install

# check for install success
RUN cp -p $(find /usr/local/lib/python3.5/site-packages -name cv2.*.so) \
	/usr/lib/python3.5/site-packages/cv2.so && \
	python -c 'import cv2; print("Python: import cv2 - SUCCESS")'

# land on opencv directory
WORKDIR /usr/src/opencv

# cleanup
RUN rm -rf /usr/src/opencv/build
