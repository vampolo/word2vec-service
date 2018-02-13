#!/bin/sh

set -ex

mkdir -p /opt/data

GOOGLENEWS_VECTORS_FILE=/opt/data/GoogleNews-vectors-negative300.bin
FASTTEXT_VECTORS_FILE_JPN = /opt/data/wiki.ja.vec

if [ "$SKIP_DATA_DOWNLOAD" != true ] && [ ! -f  "$GOOGLENEWS_VECTORS_FILE" ]; then
    wget -O /opt/data/GoogleNews-vectors-negative300.bin.gz https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz
    gunzip /opt/data/GoogleNews-vectors-negative300.bin.gz
fi

if [ "$SKIP_DATA_DOWNLOAD" != true ] && [ ! -f  "$FASTTEXT_VECTORS_FILE_JPN" ]; then
        wget -O /opt/data/wiki.ja.vec https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.ja.vec
fi

exec "$@"
