## Desafio 3 do ***Bootcamp Cloud* AWS**

Evento promovido pela [Digital Innovation One - DIO](https://www.dio.me/en), com patrocínio da [Amazon Web Services - AWS](https://aws.amazon.com/pt/).

<div align="right">
  <img src="https://github.com/crobertocamilo/linux_servidor_apache/blob/main/assets/logo_bootcamp.webp?raw=true.webp" alt="logo bootcamp" width=20%/>
</div>

--- 
## Desafio
Infraestrutura como código: **Desenvolver uma aplicação *serverless* para operações básicas (CRUD) numa tabela no AWS DynamoDB. O projeto deve considerar a criação da tabela, criação das rotas da API e permissões necessárias. Utilizar o *Serverless Framework* para a implementação, com livre escolha da linguagem de programação e tema/esquema da tabela.**

---
### Objetivo

Desenvolver uma API *serverless* para criar uma tabela e realizar operações básicas num banco de dados (inserir item, consultar, atualizar e deletar) na AWS. A aplicação deve implementar a solução através do *Serverless Framework* (sem utilizar o console da AWS) e funções Lambda, em python, para integrar os serviços API Gateway e DynamoDB.

---
### Desenvolvimento da solução:

A solução foi desenvolvida utilizando funções Lambda em **python**, uma função para cada tipo de operação sobre a tabela, sendo o código das funções apresentado na pasta [src](https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/tree/main/src). 

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/aws_services.png?raw=true" alt="Estrutura de serviços na AWS" width=85%/>
</div>

<div align="center">
Integração da API com o bando de dados através de função Lambda. 
</div>

<br></br>
A integração entre os serviços da AWS é realizada através do **Serverless Framework**. O arquivo [serverless.yml](https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/serverless.yml) define a estrutura de recursos (**API Gateway**, **Lambda**, **DynamoDB**) e é utilizado para a criação de uma estrutura de serviços (*stack*) no **CloudFormation**, compreendendo também criação das permissões necessárias no **IAM** e registro de *logs* no **CloudWatch**.

---
### Implementando a solução:

Requisitos:
* Serverless Framework instalado (tutorial oficial [aqui](https://www.serverless.com/framework/docs/tutorial));
* AWS-CLI [instalado](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) e configurado com as credenciais da conta (Access Key e Secret Key) na AWS. Para mais informações, clique [aqui](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/).

<br></br>

Para o *deploy* da solução na AWS, clone este repositório e acesse a pasta raiz pelo terminal. Digite:

  `serverless deploy`

Se a estrutura de serviços for construída com sucesso em sua conta da AWS, será exibido no terminal uma mensagem como a mostrada abaixo, onde são listados os *endpoints* criados para cada método/operação no banco de dados. 

Os links mostrados na imagem são apenas exemplos e não estão mais disponíveis.

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/serverless_deploy.png?raw=true" alt="Estrutura de serviços na AWS" width=70%/>
</div>

---
### Utilizando a API:

Como este projeto não compreende o desenvolvimento de um *front-end*, a interação com os *endpoints* da API deve ser feita através de um navegador (GET) ou utilizando uma ferramenta para testar APIs, como por exemplo o [**Postman**](https://www.postman.com/).

O DynamoBD é um banco de dados NoSQL do tipo chave-valor, por isso seus objetos seguem a estrutura *"nomeChave": "valorAtributo"*. Não é necessário que todos os registros tenham todos os atribuitos pois as tabelas no DynamoBD não possuem um esquema rígido. Neste exemplo, o único campo obrigatório é *Cidade*, que á chave primária da tabela (*partition key*) e o *id* dos registros.

<br></br>

#### **> Inserindo itens (*insertItem*)**

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/insert.png?raw=true" alt="Inserindo um registro" width=60%/>
</div>

<div align="center">
Inserindo um novo registro na tabela. 
</div>

<br></br>

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/insert_table.png?raw=true" alt="Novo registro inserido na tabela" width=45%/>
</div>
<div align="center">
Novo registro salvo no DynamoDB.
</div>

<br></br>

#### **> Pesquisando item pelo id (*getItem*)**

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/get2_highlights.png?raw=true" alt="Pesquisando pelo id - Sucesso" width="70%"/>
</div>

<div align="center">
Pesquisando um registro pelo id (uma Cidade pelo nome): SUCESSO. 
</div>

<br></br>

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/get3_highlights.png?raw=true" alt="Pesquisando pelo id - Erro" width="70%"/>
</div>

<div align="center">
Pesquisando um registro pelo id: ERRO. 
</div>

<br></br>

#### **> Listando os itens da tabela (*fetchItems*)**

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/fetch_highlights.png?raw=true" alt="Listando itens da tabela" width="65%"/>
</div>

<div align="center"> 
Lista (trecho) dos itens salvos da tabela.
</div>

<br></br>

#### **> Alterando um registro (*updateItem*)**

<table>
  <tr>
    <td>
      <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/update1_highlights.png?raw=true" alt="Modificando registro 1" width="100%">
    </td>
    <td>
      <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/update2_highlights.png?raw=true" alt="Modificando registro 2" width="100%">
    </td>
  </tr>
</table>
<div align="center">
Modificando registros da tabela.
</div>

<br></br>

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/update_table_highlights.png?raw=true" alt="Pesquisando pelo id - Erro" width="50%"/>
</div>

<div align="center">
Tabela atualizada com as alterações. 
</div>

<br></br>
#### **> Removendo um registro (*deleteItem*)**

<div align="center">
  <img src="https://github.com/crobertocamilo/Serverless-CRUD-AWS-Python/blob/main/assets/delete.png?raw=true" alt="Deletando um registro" width="65%"/>
</div>

<div align="center"> 
Deletando um registro.
</div>

  