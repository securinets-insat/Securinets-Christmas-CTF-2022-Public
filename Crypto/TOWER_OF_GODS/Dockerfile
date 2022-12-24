FROM python:alpine3.16
RUN apk update
RUN apk upgrade
RUN apk add build-base
RUN apk add socat

RUN adduser -h /home/somebody -s /bin/bash ctf -u 1001 | echo raf | echo raf

WORKDIR /home/ctf

COPY . .

USER ctf

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 server.py ">/dev/null