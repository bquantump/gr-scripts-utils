FROM ubuntu:20.04

LABEL maintainer="bquantump@github.com"
LABEL version="0.1"
LABEL description="Gr-Vita image."

ARG gnuradio_hash
ARG volk_hash
ARG DEBIAN_FRONTEND=noninteractive


RUN apt-get update -y && apt update && apt-get install -y apt-utils

#RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

#USER docker
#CMD /bin/bash

RUN apt install -y git cmake g++ libboost-all-dev libgmp-dev swig python3-numpy \
python3-mako python3-sphinx python3-lxml doxygen libfftw3-dev \
libsdl1.2-dev libgsl-dev libqwt-qt5-dev libqt5opengl5-dev python3-pyqt5 \
liblog4cpp5-dev libzmq3-dev python3-yaml python3-click python3-click-plugins \
python3-zmq python3-scipy python3-gi python3-gi-cairo gobject-introspection gir1.2-gtk-3.0 && \
apt install -y pybind11-dev python3-matplotlib libsndfile1-dev && \
apt install -y libcodec2-dev libgsm1-dev && apt-get -y install python3-pip && apt install -y python3-venv && \
apt-get install sudo -y

RUN apt update && ldconfig

RUN mkdir git && cd git && git clone --recursive https://github.com/gnuradio/volk.git && \
cd volk && git checkout ${volk_hash} && mkdir build && cd build && \
cmake -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 ../ && make -j16 &&  make install

RUN cd git && git clone https://github.com/gnuradio/gnuradio.git && cd gnuradio && \
git checkout ${gnuradio_hash} && mkdir build && cd build && \ 
cmake -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 ../ && make -j16 &&  make install


EXPOSE 80 443
