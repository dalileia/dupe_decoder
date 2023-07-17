#!/bin/bash

cd /opt/dupedecoder/app
OPT="$1"

check_conditions() {
	MY_CURRENT_USER=`whoami`

	if [ "$MY_CURRENT_USER" != "root" ] ; then
		echo "Obtenha acessos administrativos antes de efetuar do deploy."
		echo "Utilize o comando 'sudo su' e depois execute este script novamente."

		exit 1
	fi

	if [ "$ENV_PRODUCTION" = "yes" ] ; then
		echo "Starting DUPEDECODER deployment..."
	else
		echo "Do not run this script in dev mode."
		exit 2
	fi

}

function usage() {

    echo "Utilize os comandos abaixo:"
    echo "  'build': Atualiza o git e então efetua o build do backend e portal."
    
    read OPT
    choose_option

}

function do_build() {
	bash ./deploy/docker-down-container.sh && \
	bash ./deploy/update-git.sh && \
	bash ./deploy/deploy-backup-database.sh /mysql_data/mysql /mysql_data/mysql-backup && \
	bash ./deploy/docker-up-container.sh
}

function choose_option() {
    case "$OPT" in
        "build")
            do_build;;
        "")
            usage;;
        *)
			echo "Exit"
            exit 0;;
    esac
}


check_conditions
usage

