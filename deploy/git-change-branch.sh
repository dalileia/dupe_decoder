#!/bin/bash

if [ "$ENV_PRODUCTION" = "yes" ] ; then
    cd /opt/dupedecoder/app

    echo "Para qual branch deseja mudar? Deixe vazio para utilizar a *main*"
	read GIT_REPO_BRANCH

    if test -z "$GIT_REPO_BRANCH" 
    then
        GIT_REPO_BRANCH="main"
    fi

	git fetch origin
    git checkout origin/$GIT_REPO_BRANCH
    git switch $GIT_REPO_BRANCH

    git reset --hard
    git submodule foreach --recursive git reset --hard
    git submodule update --recursive --init

fi

