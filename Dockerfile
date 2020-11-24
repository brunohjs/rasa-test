FROM python:3.8-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download pt_core_news_lg
COPY . .
VOLUME /tmp
EXPOSE 5005 5055
RUN rasa train