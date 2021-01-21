FROM python:3.9-slim-buster
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y -qq install \
    build-essential \
    clamav-daemon && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/clamav && \
    chown clamav:clamav /var/run/clamav && \
    chmod 750 /var/run/clamav

COPY ./include/clamd.conf /etc/clamav/clamd.conf
COPY ./requirements.txt /
RUN pip install -r /requirements.txt
COPY app/ /app
WORKDIR /app
RUN pip install --no-deps /app/
RUN pip freeze

ENTRYPOINT ["uvicorn", "clamapi:app", "--reload", "--host", "0.0.0.0"]
