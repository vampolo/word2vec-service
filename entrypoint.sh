#!/bin/sh

set -ex

mkdir -p /opt/data

GOOGLENEWS_VECTORS_FILE=/opt/data/GoogleNews-vectors-negative300.bin

if [ "$SKIP_DATA_DOWNLOAD" != true ] && [ ! -f  "$GOOGLENEWS_VECTORS_FILE" ]; then
    curl -o - https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz | gunzip > /opt/data/GoogleNews-vectors-negative300.bin
fi

exec "$@"
