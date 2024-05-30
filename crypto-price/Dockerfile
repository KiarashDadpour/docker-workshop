FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip python3-pandas python3-requests
ENV PIP_DEFAULT_TIMEOUT=100
RUN mkdir /my-app
WORKDIR /my-app
COPY main.py .
ENTRYPOINT python3 main.py
