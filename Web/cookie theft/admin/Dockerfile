FROM ubuntu:18.04
WORKDIR /chafra

RUN apt-get update && \
    apt install -y curl \
                       curl \
                       g++ \
                       unixodbc-dev \
                       python3-pip \
                       python3


#RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
#RUN curl https://packages.microsoft.com/config/ubuntu/18.04/mssql-server-2019.list > /etc/apt/sources.list.d/mssql-server-2019.list

#RUN apt update -y
#RUN ACCEPT_EULA=Y apt install -y msodbcsql18 mssql-tools18 unixodbc-dev 


COPY . .
RUN pip3 install -r requirement.txt

CMD [ "python3", "main.py"]

