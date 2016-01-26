FROM ubuntu:14.04
MAINTAINER ipinak

LABEL version=1.0.0
LABEL description="This is a crawler application for naftemporiki.gr"

# Prepare the environment
RUN apt-get update \
    && apt-get install -y python python-dev git-core wget \
    && wget https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && pip install -r requirements.txt

VOLUME ["/data"]

CMD ["/bin/sh", "-c", "/naftis/run.sh"]


