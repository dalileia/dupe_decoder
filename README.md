***

chmod 400 key-dupedecoder.pem
Para acessar o servidor

ssh -i key-dupedecoder.pem ubuntu@18.229.54.106

## Configuração de ambiente ##
A primeira coisa que você vai fazer quando precisar configurar um novo servidor

- Instancie uma Maquina UBUNTU LTS na nuvem da sua preferencia
- Acesse o terminal da máquina
- Solicite poderes administrativos: `sudo su`
- Crie a pasta da aplicação: `mkdir /opt/dupedecoder`
- Acesse a pasta da aplicação:  `cd /opt/dupedecoder`
- Crie o arquivo de setup de ambiente: `nano setup.sh`
- Copie e cole o conteúdo do arquivo setup.sh no editor de texto que aparece no terminal
- Saia do Nano utilizando CTRL+X, pressionando Y para confirmar o nome do arquivo.
- Execute o novo arquivo setup.sh: `bash setup.sh`
- Escolha a opção `easy` se for a primeira execução do ambiente de configuração
- Insira o endereço do repositório quando for solicitado: `git@github.com:dalileia/product_compare_python.git`
- Siga qualquer outra instrução que surgir até o fim do script.

A partir deste ponto a sua aplicação está pronta para deploy



## Efetuando Deploy ##
Os acessos subsequentes serão com estas instruções:

- Acesse o terminal da máquina
- Solicite poderes administrativos: `sudo su`
- Acesse a pasta da aplicação:  `cd /opt/dupedecoder/app`
- Execute o script de deploy e siga as instruções: `bash deploy.sh`
