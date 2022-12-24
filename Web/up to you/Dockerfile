FROM php:7.0-apache
COPY src/ /var/www/html
RUN chmod 755 /var/www/html
RUN groupadd -r swuser -g 433 && \
    useradd -u 431 -r -g swuser -s /sbin/nologin -c "Docker image user" swuser
USER swuser
EXPOSE 80


