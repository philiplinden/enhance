FROM python:3.6-alpine

# update apt-get index
RUN apt-get update

# install developer tools
RUN apt-get install -y \
	build-essential \
	cmake \
	unzip \
	pkg-config

# install image, video and I/O libraries
RUN apt-get install -y \
	libjpeg-dev \
	libpng-dev \
	libtiff-dev \
	libavcodec-dev \
	libavformat-dev \
	libswscale-dev \
	libv4l-dev \
	libxvidcore-dev \
	libx264-dev \
	libgtk-3-dev \
	libatlas-base-dev \
	gfortran \
	python3-dev

# install python dependencies
RUN pip install -y \
	numpy

# OpenCV Version
ENV OPENCV_VERSION 4.2.0

# download and extract OpenCV core
RUN wget -O /usr/src/opencv-tmp/opencv.zip https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip \
	&& unzip /usr/src/opencv.zip \
	&& mv /usr/src/opencv-tmp/opencv-${OPENCV_VERSION} /usr/src/opencv

# download and extract OpenCV contrib
RUN wget -O /usr/src/opencv-tmp/opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/${OPENCV_VERSION}.zip \
	&& unzip /usr/src/opencv-tmp/opencv_contrib.zip \
	&& mv /usr/src/opencv-tmp/opencv_contrib-${OPENCV_VERSION} /usr/src/opencv_contrib

WORKDIR /usr/src/opencv/build

# configure compilation options
RUN cmake \
	-D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D OPENCV_EXTRA_MODULES_PATH=usr/src/opencv_contrib/modules \
	-D PYTHON3_LIBRARY=`python -c 'import subprocess ; import sys ; s = subprocess.check_output("python-config --configdir", shell=True).decode("utf-8").strip() ; (M, m) = sys.version_info[:2] ; print("{}/libpython{}.{}.dylib".format(s, M, m))'` \
	-D PYTHON3_INCLUDE_DIR=`python -c 'import distutils.sysconfig as s; print(s.get_python_inc())'` \
	-D PYTHON3_EXECUTABLE=usr/local/bin/python \
	-D BUILD_opencv_python2=OFF \
	-D BUILD_opencv_python3=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D BUILD_EXAMPLES=ON ..

# compile
RUN make

# install
RUN make install

# land on opencv directory
WORKDIR /usr/src/opencv
