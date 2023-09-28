# MVP 03 - Project HomeBroker 

Projeto de uma aplicação responsavel por comprar e vender ações.

---

## Componente B: Stocks Service
 + Responsável por consultar informações de preços de ações individuais na Nasdaq;
 + Oferece uma lista das cinco ações mais populares na Nasdaq com base em dados em tempo real;
 + Utiliza uma API externa para obter informações de mercado atualizadas.

---
### Uso da API Externa:

Este projeto utiliza a API externa [Alpha Vantage](https://www.alphavantage.co/) para obter informações sobre preços de ações 
listadas na Nasdaq.

A API é gratuita, mas requer um registro para obter uma chave de API (API Key) para acesso.

Para obter uma API Key da Alpha Vantage, siga estas etapas:

 - Acesse o site da Alpha Vantage em https://www.alphavantage.co/.

 - Clique na seção "Get Free API Key" ou clique [aqui](https://www.alphavantage.co/support/#api-key) para ir direto 
para a sessão de castro para iniciar o processo de registro.

 - Preencha as informações necessárias, incluindo e-mail.

 - Será fornecido a API Key. Abra o arquivo .env e insira a sua API Key. 

---


### Execução através do Docker:

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) 
instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
docker build -t stocks-service .
```

Caso nao esteja criada, execute o comando abaixo, para a criação de uma nova
network:

```
docker network create <my_network> 
```

Para a execução o container basta executar, **como administrador**, seguinte o comando:

```
docker run -p 5001:5001 --name stocks-service --network <my_network> stocks-service
```
