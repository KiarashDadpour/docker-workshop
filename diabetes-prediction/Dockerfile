FROM ubuntu
 
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-pandas python3-sklearn

RUN mkdir /ML-app
WORKDIR /ML-app

COPY . /ML-app
# optional 
EXPOSE 80 
