FROM tensorflow/tensorflow:1.13.2-gpu-py3


# apt install
RUN apt-get -y update && \
        apt -y install git \
                vim


# pip3 install ML lib
ENV SCIKIT_IMAGE_VER=0.15.0
ENV SCIPY_VER=1.2.1
ENV SCIKIT_LEARN_VER=0.21.3
ENV KERAS_VER=2.2.4

RUN pip3 install scikit-image==${SCIKIT_IMAGE_VER} \
                scipy==${SCIPY_VER} \
                scikit-learn==${SCIKIT_LEARN_VER} \
                keras==${KERAS_VER}


# pip3 install python lib
ENV BOTOCORE_VER=1.10.84
ENV BOTO3_VER=1.7.84

RUN pip3 install botocore==${BOTOCORE_VER} \
                boto3==${BOTO3_VER}


# folder
RUN mkdir /src
COPY . /src
WORKDIR /src
