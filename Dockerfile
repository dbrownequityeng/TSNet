from python:3.9-buster

RUN apt-get update && \
    apt-get install -y  gcc g++ gfortran nano
    
RUN pip install --upgrade pip &&\
    pip install numpy 

RUN wget https://github.com/USEPA/WNTR/archive/refs/tags/0.5.0.tar.gz && \ 
    tar -xvf 0.5.0.tar.gz && cd  ./WNTR-0.5.0 &&\
    python setup.py develop --build

RUN git clone https://github.com/dbrownequityeng/TSNet.git && \ 
    cd ./TSNet && \
    python setup.py install

WORKDIR /root/shared

#0.2.3 WNTR-->0.5.0
