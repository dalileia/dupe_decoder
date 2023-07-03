#!/bin/bash

MYSQL_PATH=$1
MYSQL_BACKUP_PATH=$2

echo "CREATING $MYSQL_PATH BACKUP..."

TS=$(date +"%Y_%m_%d.%H%M%S%3N")
BACKUP_FILE_NAME="BACKUP-$TS.tgz"

CUR_PATH=`pwd`

mkdir -p $MYSQL_PATH
mkdir -p $MYSQL_BACKUP_PATH

cd $MYSQL_PATH
tar -zcf "BACKUP-$TS.tgz" ./*

cd $CUR_PATH
mv "$MYSQL_PATH/$BACKUP_FILE_NAME" $MYSQL_BACKUP_PATH

echo " but its okay!"
echo ""
echo "BACKUP DONE AT $MYSQL_BACKUP_PATH/$BACKUP_FILE_NAME"
echo ""
