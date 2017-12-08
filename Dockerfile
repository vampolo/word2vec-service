FROM alpine
LABEL maintainer="vincenzo.ampolo@gmail.com"

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python3", "/app/main.py"]

RUN apk add --no-cache python3 wget gzip openblas libstdc++
RUN python3 -m ensurepip --upgrade

COPY requirements.txt /

RUN apk add --no-cache --virtual .build-dependencies gcc gfortran python3-dev build-base freetype-dev libpng-dev openblas-dev

RUN python3 -m pip install -r requirements.txt

RUN apk del .build-dependencies

COPY entrypoint.sh /
COPY src /app
