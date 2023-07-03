#!/bin/bash

if [ "$ENV_PRODUCTION" = "yes" ] ; then
    cd /opt/dupedecoder/app
	
	CURRENT_BRANCH=`git rev-parse --abbrev-ref HEAD`
	
	git fetch origin
	git reset --hard origin/$CURRENT_BRANCH

    git submodule foreach --recursive git reset --hard
    git submodule update --recursive --init
fi

