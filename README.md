## Desafio 2 do ***Bootcamp Cloud* AWS**

Evento promovido pela [Digital Innovation One - DIO](https://www.dio.me/en), com patrocínio da [Amazon Web Services - AWS](https://aws.amazon.com/pt/).

<div align="right">
  <img src="https://github.com/crobertocamilo/linux_servidor_apache/blob/main/assets/logo_bootcamp.webp?raw=true.webp" alt="logo bootcamp" width=20%/>
</div>

--- 
## Desafio
**Infraestrutura como código: Desenvolver uma aplicação *serverless* para operações básicas (CRUD) numa tabela no AWS DynamoDB. O projeto deve considerar a criação da tabela, criação das rotas da API e permissões necessárias. Utilizar o *Serverless Framework* para a implementação, com livre escolha da linguagem de programação e tema/esquema da tabela.**

---
### Objetivo

Desenvolver uma API *serverless* para criação e operações básicas num banco de dados (inserir item, consultar, atualizar e deletar) na AWS. A aplicação deve implementar a solução através do *Serverlesse Framework* (sem utilizar o console da AWS) e funções Lambda, em python, para integrar os serviços API Gateway e DynamoDB.

---
### Desenvolvimento da solução:

A solução foi desenvolvida utilizando funções Lambda em **python**, uma função para cada tipo de operação sobre a tabela, sendo o código das funções apresentado na pasta [src/](https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/tree/main/src). 

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/aws_services.png?raw=true" alt="Estrutura de serviços na AWS" width=100%/>
</div>

<div align="center">
Integração da API com o bando de dados através de função Lambda. 
</div>

<br></br>
A integração entre os serviços da AWS é realizada através do **Serverless Framework**. O arquivo [serverless.yml](https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/serverless.yml) define a estrutura de recursos (**API Gateway**, **Lambda**, **DynamoDB**) e é utilizado para a criação de uma estrutura de serviços (*stack*) no **CloudFormation**, compreendendo também criação das permissões necessárias no **IAM** e registro de *logs* no **CloudWatch**.

---
### Implementando a solução:

Requisitos:
* Serverless Framework instalado;
* AWS CLI instalado e configurado com as credenciais da conta (AccessKey e )

Para o *deploy* da solução na AWS, clone este repositório e acesse a pasta raiz pelo terminal. Digite:

`serverless deploy`

Se a estrutura de serviços for construída com sucesso em sua conta da AWS, será exibido no terminal uma mensagem como a mostrada abaixo, onde são listados os *endpoints* criadas para cada método/operação no banco de dados. 

Os links mostrados na imagem são apenas exemplos e não estão mais disponíveis.

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/serverless_deploy.png?raw=true" alt="Estrutura de serviços na AWS" width=80%/>
</div>


