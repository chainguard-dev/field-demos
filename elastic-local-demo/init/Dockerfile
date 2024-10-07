FROM cgr.dev/chainguard-private/elasticsearch:8.15.1-dev

# become the root user
USER root

# set working directory
WORKDIR /usr/share/elasticsearch

# make the directories needed
RUN mkdir -p /usr/share/elasticsearch/config/certs
RUN mkdir -p /usr/share/elasticsearch/data

# copy config needed to boostrap certificates
COPY instances.yml config/certs/instances.yml

# create certificate authority and certificates
RUN if [ ! -f config/certs/ca/ca.crt ]; then elasticsearch-certutil ca --silent --pem -out config/certs/ca.zip && unzip config/certs/ca.zip -d config/certs; fi
RUN elasticsearch-certutil cert --silent --pem --in config/certs/instances.yml --out config/certs/certs.zip --ca-cert config/certs/ca/ca.crt --ca-key config/certs/ca/ca.key && unzip config/certs/certs.zip -d config/certs

# change permissions
RUN chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/
RUN find config/certs -type d -exec chmod 750 {} \; ; find config/certs -type f -exec chmod 640 {} \;

# become nonroot again
USER elasticsearch
