# The base image of this Dockerfile is Ubuntu, which we used to teach the concept of Dockerfile layering.
# However, to run Python code more efficiently, we can now use a Python base image.
# Base Image: Ubuntu
FROM ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip python3-pandas python3-requests
ENV PIP_DEFAULT_TIMEOUT=100
RUN mkdir /my-app
WORKDIR /my-app
COPY main.py .
ENTRYPOINT python3 main.py
# Base Image: Python
FROM python:3.9-slim
RUN mkdir /my-app
WORKDIR /my-app
RUN pip install pandas
RUN pip install requests
COPY main.py .
ENTRYPOINT python3 main.py
