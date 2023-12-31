FROM ubuntu:22.04

RUN apt update && apt full-upgrade -y \
    python3 \
    python3-pip

RUN apt install default-libmysqlclient-dev -y
    
COPY requirements.txt /var/app/requirements.txt

WORKDIR /var/app

COPY ./app /var/app

RUN pip3 install -r requirements.txt

