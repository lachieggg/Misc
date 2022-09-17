#!/bin/bash

# Open a console in the container

cd $GIT/MailServer
docker exec -it mailserver bash
