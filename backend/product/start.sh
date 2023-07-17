#!/bin/bash

if [ "$ENV_PRODUCTION" = "yes" ] ; then
	uwsgi --ini python.ini
else
    export FLASK_DEBUG=1
    sleep 15s
    yoyo init --database mysql://root:@mysql/product migrations
    yoyo apply
    flask --app app run --host 0.0.0.0 --port 5000
fi