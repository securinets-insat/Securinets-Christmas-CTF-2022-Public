FROM alpine
RUN apk update
RUN apk upgrade
RUN apk add socat
# RUN apk add build-base


RUN adduser -h /home/somebody -s /bin/bash ctf -u 1001 | echo raf | echo raf

WORKDIR /home/ctf

COPY secret.txt .


COPY server.py . 

RUN rm secret.txt

USER ctf

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"cat server.py ">/dev/null