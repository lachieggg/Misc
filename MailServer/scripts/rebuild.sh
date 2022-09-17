#!/bin/bash

cd $GIT/MailServer
docker image rm -f mailserver_mailserver
docker-compose up -d
