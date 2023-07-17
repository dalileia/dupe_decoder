#!/bin/bash

if [ "$ENV_PRODUCTION" = "yes" ] ; then
    cd /opt/dupedecoder/app/
    yes | docker compose -f docker-compose.yml -f production.yml up -d
fi

