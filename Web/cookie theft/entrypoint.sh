#!/bin/bash
sudo docker network create dbweb
#-v /home/nzeros/Desktop:/var/opt/mssql
sudo docker stop bot
sudo docker rm bot
sudo docker build -t bot ./bot
sudo docker run -d --name bot2 -e COOKIE_DOMAIN:webadmin -e COOKIE_KEY:flag -e COOKIE_VALUE:Securinets{nice_thEft_aMigo} --net dbweb bot
sudo docker build -t webadmin2 ./admin
sudo docker build -t webpublic2 ./public/chafra
sudo docker stop webadmin
sudo docker rm webadmin
sudo docker stop webpublic
sudo docker rm webpublic
sudo docker run -d --name webadmin --read-only --net dbweb webadmin:latest
#sudo docker run -d --name webadmin --net dbweb -e SERVER=db,1433 -e USER=SA -e PASSW=n0s@nzeros123 webadmin:latest
sudo docker run -d -p 5050:5000 -e URL_BOT=http://bot:5000/visit --read-only --name webpublic --net dbweb webpublic:latest
#sudo docker run -d -p 80:5000 -e URL_BOT=http://bot:5000/visit --name webpublic --net dbweb webpublic:latest
exit