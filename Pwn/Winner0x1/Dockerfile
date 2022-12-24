FROM ubuntu AS app

FROM pwn.red/jail
COPY --from=app / /srv

COPY winner1 /srv/app/run
COPY flag.txt /srv/app/flag.txt
