FROM ubuntu:14.04
MAINTAINER ipinak

# Prepare the environment
RUN apt-get update\
    && apt-get install -y python python-dev git-core wget\
    && wget https://bootstrap.pypa.io/get-pip.py\
    && python get-pip.py\
    && apt-get clean\
    && git clone https://github.com/ipinak/naftis naftis\
    && cd naftis\
    && pip install -r requirements.txt\
    && mkdir -p /var/tmp/supervisor

VOLUME ["/data"]

ADD run.sh /run.sh
RUN chmod a+x /run.sh

ENTRYPOINT ["./run.sh"]
