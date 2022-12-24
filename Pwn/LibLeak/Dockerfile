FROM ubuntu AS app

FROM pwn.red/jail
COPY --from=app / /srv

COPY libleak /srv/app/run
COPY ld-linux-x86-64.so.2 /srv/app/ld-linux-x86-64.so.2
COPY libc.so.6 /srv/app/libc.so.6
COPY flag.txt /srv/app/flag.txt
