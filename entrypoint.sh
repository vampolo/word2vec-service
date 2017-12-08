#!/bin/sh

set -eux

mkdir -p /opt/data

cd /tmp
git clone https://github.com/mmihaltz/word2vec-GoogleNews-vectors.git
cd word2vec-GoogleNews-vectors
zcat GoogleNews-vectors-negative300.bin.gz > /opt/data/GoogleNews-vectors-negative300.bin

cd /

exec "$@"
