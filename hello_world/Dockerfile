# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /hello_world

# Set the working directory to /hello_world
WORKDIR /hello_world

# Copy the current directory contents into the container at /hello_world
ADD . /hello_world/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# FROM oraclelinux:7-slim
ENV ORACLE_HOME=/usr/lib/oracle/12.2/client64
ENV PATH=$PATH:$ORACLE_HOME/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME/lib
ADD oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm /tmp/
ADD oracle-instantclient12.2-sqlplus-12.2.0.1.0-1.x86_64.rpm /tmp/
ADD oracle-instantclient12.2-devel-12.2.0.1.0-1.x86_64.rpm /tmp/
# Setup locale, Oracle instant client and Python
RUN apt-get update \
    && apt-get -y install alien libaio1 \
    && alien -i /tmp/oracle-instantclient12.2-basic-12.2.0.1.0-1.x86_64.rpm \
    && alien -i /tmp/oracle-instantclient12.2-sqlplus-12.2.0.1.0-1.x86_64.rpm \
    && alien -i /tmp/oracle-instantclient12.2-devel-12.2.0.1.0-1.x86_64.rpm \
    && ln -snf /usr/lib/oracle/12.2/client64 /opt/oracle \
    && mkdir -p /opt/oracle/network \
    && ln -snf /etc/oracle /opt/oracle/network/admin \
    && pip install cx_oracle \
    && apt-get clean && rm -rf /var/cache/apt/* /var/lib/apt/lists/* /tmp/* /var/tmp/*
ADD root /

