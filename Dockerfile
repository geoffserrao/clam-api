FROM python:3.9-slim-buster
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y -qq install \
    clamav-freshclam \
    clamav-daemon && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/clamav && \
    chown clamav:clamav /var/run/clamav && \
    chmod 750 /var/run/clamav

COPY ./include/bootstrap.sh /
USER clamav
ENTRYPOINT ["/bootstrap.sh"]
