#!/bin/bash

if [ "$ENV_PRODUCTION" = "yes" ] ; then
	uwsgi --ini python.ini
else
    export FLASK_DEBUG=1
    flask --app app run --host 0.0.0.0 --port 5000
    yoyo init --database mysql://root:@mysql/product migrations
    chmod 777 migrations yoyo.ini __pycache__ ./app/__pycache__ ./migrations/__pycache__
fi