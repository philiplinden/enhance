# install python 3.6.5

# install prerequisites (to build opencv) 
## with homebrew for macos
cmake pkg-config jpeg libpng libtiff openexr eigen tbb wget

## with apt-get for linux
### developer tools
build-essential cmake unzip pkg-config

### image, video and I/O libraries
libjpeg-dev libpng-dev libtiff-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev

# python prerequisites (pip install ___)
numpy

# download and extract opencv
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.2.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.2.0.zip

unzip opencv.zip
unzip opencv_contrib.zip

mv opencv-4.2.0 opencv
mv opencv_contrib-4.2.0 opencv_contrib

cd opencv
mkdir build
cd build

# configure makefile
Note! `OPENCV_ENABLE_NONFREE` enables use of features that are
licensed for **educational use only**. be careful.

cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=./opencv_contrib/modules \
    -D PYTHON3_LIBRARY=`python -c 'import subprocess ; import sys ; s = subprocess.check_output("python-config --configdir", shell=True).decode("utf-8").strip() ; (M, m) = sys.version_info[:2] ; print("{}/libpython{}.{}.dylib".format(s, M, m))'` \
    -D PYTHON3_INCLUDE_DIR=`python -c 'import distutils.sysconfig as s; print(s.get_python_inc())'` \
    -D PYTHON3_EXECUTABLE=$VIRTUAL_ENV/bin/python \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D BUILD_EXAMPLES=ON ..

# compile (multithreaded)
make -j4

# install
sudo make install