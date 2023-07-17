#!/bin/bash

# roteiro para configuração de ambiente do host
# este scritp deve ser utilizado sempre que for necessario setar uma nova maquina de deploy

# COMO UTILIZAR:
# Copie este arquivo para a maquina que será o host do projeto e execute-o


start_up() {
	clear
	echo "ATENÇÃO: Execute esse script apenas na maquina virtual de HOMOLOG OU PRODUÇÃO."
	echo "  O que deseja fazer?"
	echo "     easy : Executa os comandos iniciais de configuracao em sequencia."
	echo "     create-swap : Configura memoria Swap"
	echo "     setup-machine : Instalar Docker e outras dependencias"
	echo "     ssh-key : Cria ou expõe a chave de acesso SSH para o repositório"
	echo "     clone-repo : Baixar repositorio"
	echo "     set-to-production : Definir ambiente para PRODUCAO"
	echo "     upgrade-docker : Upgrade Docker Engine quando necessário"
	echo "     exit : Sair"
	echo ""
	
	read option
	
	case $option in
		"easy")
			do_create_swap
			do_setup_machine
			do_recreate_key
			do_clone_repository
			do_set_production

			;;
		"exit")
			exit
			;;
		"clone-repo")
			do_clone_repository
			;;
		"create-swap")
			do_create_swap
			;;
		"upgrade-docker")
			echo "Atualizando Docker Engine..."
			do_upgrade_docker
			;;
		"setup-machine")
			do_setup_machine
			;;
		"set-to-production")	
			do_set_production
			;;
		"ssh-key")
			do_recreate_key
			;;
		*)
			start_up
			;;
	esac
}

check_user() {
  my_user=`whoami`

  if [ "$my_user" != "root" ] ; then
    echo "Execute o script usando o comando sudo su"
    exit 1;
  else
	start_up
  fi
}

do_create_swap() {
	has_swap=`sudo swapon --show`
	
	if [ "$has_swap" = "" ] ; then 
		
		sudo fallocate -l 6G /swapfile
		sudo chmod 600 /swapfile
		sudo mkswap /swapfile
		sudo swapon /swapfile
		
		sudo swapon --show
		free -h
		
		sudo cp /etc/fstab /etc/fstab.bak
		echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
		
	else 
		echo ""
		echo "Este ambiente ja possui memoria Swap"
		echo ""
		echo ""
		sudo swapon --show
		echo ""
		echo ""
		free -h
		echo ""
		echo ""
	fi
	
}

do_set_production() {
	if [ ! "$ENV_PRODUCTION" = "yes" ] ; then
		echo ""
		echo "Ambiente de desenvolvimento setado"
		echo "Desligue completamente esta máquina e ligue novamente"
		echo "para que as novas variáveis de ambiente estejam disponíveis"
		echo ""
		
		echo "" >> /etc/environment
		echo "# PRODUCTION "  >> /etc/environment
		echo "export ENV_PRODUCTION=yes" >> /etc/environment
		echo "export ENV_DEVELOPE=no" >> /etc/environment

		export ENV_PRODUCTION=yes
		export ENV_DEVELOPE=no
		
		sleep 1s
	fi
}

do_upgrade_docker() {
	do_remove_docker_compose
	do_remove_docker
	do_install_docker
	do_install_docker_compose
}

do_remove_docker() {
	if ! command -v docker ; then
		sudo apt-get purge docker-ce docker-ce-cli containerd.io
		sudo rm -rf /var/lib/docker
		sudo rm -rf /var/lib/containerd
	fi
}

do_install_docker() {
	yes | sudo apt-get update
	yes | sudo apt-get install \
		apt-transport-https \
		ca-certificates \
		curl \
		gnupg-agent \
		software-properties-common
	
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
	curl -fsSL https://get.docker.com -o get-docker.sh
	sudo sh get-docker.sh
	
	sudo docker -v
}

do_remove_docker_compose() {
	sudo rm /usr/local/bin/docker-compose
}

do_install_docker_compose() {
	sudo apt-get update
	sudo apt-get install docker-compose-plugin
}

do_setup_machine() {
	echo ""
	
	# verificando se existe git
	
	if ! command -v git ; then
		echo ""
		echo ""
		echo ""
		echo "Instalando Git..."
		echo "################################################"
		echo ""
		echo ""
		echo ""
		
		yes | sudo apt-get update
		yes | sudo apt-get install git
	else
		echo " -- Git já instalado"
	fi
	
	# verificando se existe docker
	
	if ! command -v docker ; then
		echo ""
		echo ""
		echo ""
		echo "Instalando Docker..."
		echo "################################################"
		echo ""
		echo ""
		echo ""

		do_install_docker
		
	else
		echo " -- Docker já instalado"
	fi
	
	# verificando se existe docker-compose
	if ! command -v docker-compose ; then
		echo ""
		echo ""
		echo ""
		echo "Instalando Docker Compose..."
		echo "################################################"
		echo ""
		echo ""
		echo ""
		
		do_install_docker_compose
		
	else
		echo " -- Docker Compose já instalado"
	fi
	
}

do_recreate_key() {
	if [ ! -f ~/.ssh/id_rsa.pub ]; then
		yes | ssh-keygen -f ~/.ssh/id_rsa -q -N ""
	fi

	echo ""
	echo "Instale a seguinte chave no seu gerenciador de repositorio:"
	echo ""
	cat ~/.ssh/id_rsa.pub

	echo "Precione ENTER quando finalizar o registro da chave SSH no seu repositório..."
	read ENTER_KEY
	
}

do_clone_repository() {

	if [ -d /opt/dupedecoder/app ]; then
		echo "Pasta 'app' ja existe. Remova o repositorio antes de clonar novamente."
		exit 1
	fi

	cd /opt/dupedecoder/

	echo "Qual o caminho do repositório?"
	read GIT_REPO_PATH

	yes | git clone -b master --recurse-submodules $GIT_REPO_PATH app

}

check_user
