from python:3.9-buster

RUN apt-get update && \
    apt-get install -y  gcc g++ gfortran nano
    
RUN pip install --upgrade pip &&\
    pip install numpy 

RUN git clone https://github.com/USEPA/WNTR && \
    cd WNTR &&\
    python setup.py develop --build

# RUN git clone https://github.com/dbrownequityeng/TSNet.git && \ 
#     cd ./TSNet && \
#     python setup.py install

WORKDIR /root/shared