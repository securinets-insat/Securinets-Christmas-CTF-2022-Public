FROM python:3.8-slim-buster

WORKDIR /SSTI
RUN chmod 755 /SSTI
COPY . .
RUN pip3 install -r requirement.txt
RUN groupadd -r swuser -g 433 && \
    useradd -u 431 -r -g swuser -s /sbin/nologin -c "Docker image user" swuser


USER swuser

CMD [ "python3", "main.py"]