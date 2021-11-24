FROM python:3.8
LABEL maintainer="Kyungsoo Kim"

RUN echo 'alias ll="ls -alF"' >> ~/.bashrc

COPY . /app/

# FUNDMENTAL UPDATES
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install htop curl wget vim -y
RUN apt-get install libgl1-mesa-glx -y
RUN pip install --upgrade pip
RUN pip install git+https://github.com/hukkelas/DSFD-Pytorch-Inference.git
RUN pip install opencv-python
RUN pip install gunicorn
RUN pip install requests
RUN pip install flask
RUN pip install jupyterlab

# PACKAGE SETTING & CLOSING
WORKDIR /app
RUN python test.py