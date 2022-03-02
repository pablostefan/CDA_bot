# CDA_BOOT
## Desafio CDA 

Resumo: consistem em uma aplicação com um bot para o Telegram que consulta as tabelas do banco de dados, as tabelas foram populadas pelos arquivos csv disponibilizado. 

## Banco de dados 

Banco de dados utilizado: Oracle Database 18c Express Edition for Linux x64 disponibilizado pela Oracle. 

O banco foi instalado em um container criado pelo Docker usando a imagem disponibilizada no git hub https://github.com/oracle/docker-images/tree/main/OracleDatabase/SingleInstance. 

## Comandos SQL usado: 

Criar tabelas: create_cda_tables.sql 

Alimentar tabelas: 

Cliente: add_cliente.sql 

Produtos: add_produtos.sql 

Venda: add_venda.sql 

Venda de itens: add_venda_iten.sql 

## Bot telegram 

O bot Telegram foi feito usando a linguagem python e a biblioteca cx_Oracle, responsável pelas consultas necessárias. 

O código foi dividido em duas partes consultas.py e cda_bot.py, onde o arquivo consultas.py ficou responsável pelas consultas das tabelas e cda_bot.py por disponibilizar os resultados das consultas para os usuários. 

## Docker 

Todo o projeto se encontra em um container criado a partir de uma imagem disponibilizada no  https://github.com/oracle/docker-images/tree/main/OracleDatabase/SingleInstance. 

Os processos de criação foram embasados no README do repositório do git hub acima.   

Após efetuar as alterações necessárias, foram utilizados os comandos do Docker para gerar uma imagem a partir do container: 

Sudo docker commit; 

Sudo docker tag; 

Sudo docker push; 

Tornando minha imagem pública no link:  

https://hub.docker.com/layers/185085277/pablostefan/cdabot/cdabot/images/sha256-cbbdfae6e3daf582eeb4f8c7164cb41d3ffc8ed2bd9c1922a187661bae04f036?context=repo 

## Resultado 

Link do chat do bot: https://t.me/Challenge_CDA_bot 
