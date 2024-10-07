#!/usr/bin/env python3

import os
from elasticsearch import Elasticsearch

username = "elastic"
password = "password"

if not password:
    raise ValueError("The environment variable 'ELASTIC_PASSWORD' is not set or is empty.")

client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=(username, password),
    verify_certs=False
)

# certs are not verified because this is typically run from a local machine that doesn't mount the certs in the compose volume

print(client.info())
