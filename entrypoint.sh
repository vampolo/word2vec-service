#!/bin/sh

set -eux

mkdir -p /opt/data

if [ "$SKIP_DATA_DOWNLOAD" != true ]; then
    curl -o - https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz | gunzip > /opt/data/GoogleNews-vectors-negative300.bin
fi

exec "$@"
