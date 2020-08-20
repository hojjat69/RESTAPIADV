from python:3.7-alpine
MAINTAINER Hojjat Borhany

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-dops \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN pip install ps
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser -D user
USER user


