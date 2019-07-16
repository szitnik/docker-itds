FROM ubuntu:18.04

WORKDIR /work
ADD ./ .


RUN apt-get update \
    && apt-get install -y python3 python3-pip \
    && pip3 install flask

EXPOSE 8787

ENTRYPOINT python3 server.py