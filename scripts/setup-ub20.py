import os
import sys
import subprocess

update = 'sudo apt update'
basics = 'sudo apt install -y git cmake g++ libboost-all-dev libgmp-dev swig python3-numpy \
python3-mako python3-sphinx python3-lxml doxygen libfftw3-dev \
libsdl1.2-dev libgsl-dev libqwt-qt5-dev libqt5opengl5-dev python3-pyqt5 \
liblog4cpp5-dev libzmq3-dev python3-yaml python3-click python3-click-plugins \
python3-zmq python3-scipy python3-gi python3-gi-cairo gobject-introspection gir1.2-gtk-3.0  \
pybind11-dev python3-matplotlib libsndfile1-dev  \
libcodec2-dev libgsm1-dev  python3-pip  python3-venv  \
sudo'



volk = 'sudo mkdir git; sudo chmod 777 -R git; cd git; git clone --recursive https://github.com/gnuradio/volk.git;  \
cd volk;  git checkout 237a6fc9242ea8c48d2bbd417a6ea14feaf7314a;  mkdir build;  cd build;  \
cmake -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 ../;  make -j16;   sudo make install;'

gnu_radio = 'cd git; git clone https://github.com/gnuradio/gnuradio.git; cd gnuradio; \
git checkout c98adfbdbb88c08734a1507d6257755611b947c5; mkdir build; cd build; cmake -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 ../; make -j16; sudo make install'

xrdp = 'sudo apt install ubuntu-desktop -y; sudo apt update -y; sudo apt install xrdp -y; sudo adduser xrdp ssl-cert; sudo systemctl restart xrdpl; sudo ufw disable;'
subprocess.check_call(update.split(), shell=False)
subprocess.check_call(basics.split(), shell=False)
subprocess.check_call(volk, shell=True)
subprocess.check_call(gnu_radio, shell=True)
#subprocess.check_call(xrdp, shell=True)

    
            
