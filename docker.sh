#!/bin/bash
#Test and make dir
if [ -d /opt/docker ]
then cd /opt/docker || return
else mkdir /opt/docker
fi

cd /opt/docker || return
sleep 10 
git clone --single-branch --branch test https://github.com/fikolis/spring-petclinic.git

cd spring-petclinic || return

docker image build -t petclinic:latest .

docker container run --publish 8000:8080 --detach --name petclinic petclinic:latest
