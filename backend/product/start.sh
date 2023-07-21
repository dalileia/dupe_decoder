#!/bin/bash

if [ "$ENV_PRODUCTION" = "yes" ] ; then
    sleep 15s
    rm yoyo.ini
    yoyo init --database mysql://$ENV_MYSQL_USER:$ENV_MYSQL_PASSWORD@$ENV_MYSQL_HOST/product migrations
    yoyo apply
    uwsgi --ini python.ini
else
    export FLASK_DEBUG=1
    sleep 15s
    rm yoyo.ini
    yoyo init --database mysql://$ENV_MYSQL_USER:$ENV_MYSQL_PASSWORD@$ENV_MYSQL_HOST/product migrations
    yoyo apply
    flask --app app run --host 0.0.0.0 --port 5000
fi