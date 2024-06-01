# The base image of this Dockerfile is Ubuntu and we used it for the concept of Dockerfile layering,
# but now we can use the Python base image to run Python codes.
# Base Image: Ubuntu
FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip python3-pandas python3-requests
ENV PIP_DEFAULT_TIMEOUT=100
RUN mkdir /my-app
WORKDIR /my-app
COPY main.py .
ENTRYPOINT python3 main.py
# Base Image: Python
# FROM python:3.9-slim
# RUN mkdir /my-app
# WORKDIR /my-app
# RUN pip install pandas
# RUN pip install requests
# COPY main.py .
# ENTRYPOINT python3 main.py
