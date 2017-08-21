FROM python:2.7-alpine3.6
MAINTAINER ipinak

COPY ./ /naftis

# Prepare the environment
RUN cd naftis \
    && pip install -r requirements.txt \
    && mkdir -p /var/tmp/supervisor

VOLUME ["/data"]

ADD run.sh /run.sh
RUN chmod a+x /run.sh

ENTRYPOINT ["/bin/sh", "-c", "./run.sh"]
