FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download pt_core_news_lg

COPY app ./
COPY server.sh ./server.sh

USER root
RUN chmod -R 777 ./
USER 1001

EXPOSE 5005 5055

RUN rasa train