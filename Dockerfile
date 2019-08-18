FROM alpine
LABEL maintainer="vincenzo.ampolo@gmail.com"

EXPOSE 8000
CMD ["python3", "/app/main.py"]
ENV VECTOR_FILE=https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz \
    BINARY_VECTOR_FILE=true

COPY requirements.txt /

RUN set -x \
    && apk add --no-cache python3 openblas libstdc++ \
    && python3 -m ensurepip --upgrade \
    && apk add --no-cache --virtual .build-dependencies gcc gfortran python3-dev build-base freetype-dev libpng-dev openblas-dev \
    && python3 -m pip install -r requirements.txt \
    && apk del .build-dependencies

COPY src /app
