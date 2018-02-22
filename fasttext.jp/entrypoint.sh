#!/bin/sh

set -ex

mkdir -p /opt/data

FASTTEXT_VECTORS_FILE_JPN = /opt/data/wiki.ja.vec

if [ "$SKIP_DATA_DOWNLOAD" != true ] && [ ! -f  "$FASTTEXT_VECTORS_FILE_JPN" ]; then
        wget -O /opt/data/wiki.ja.vec https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.ja.vec
fi

exec "$@"
