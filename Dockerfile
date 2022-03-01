# syntax=docker/dockerfile:1
FROM python:3.9
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED=1

RUN mkdir /survey_docker

WORKDIR /survey_docker
ADD . /survey_docker/
RUN pip install -r requirements.txt