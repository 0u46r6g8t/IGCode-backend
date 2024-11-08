<div align="center">

# Como criar ambientes de desenvolvimento

</br>
</br>

<div align="left">


## <img src="https://seeklogo.com/images/D/docker-logo-CF97D0124B-seeklogo.com.png" width="25"/> Docker

O Docker é uma plataforma de código aberto que permite automatizar o processo de criação, implantação e execução de aplicativos em containers. Os containers fornecem uma maneira consistente de empacotar o código, as configurações e as dependências de um aplicativo, permitindo que ele seja executado em qualquer ambiente. Com o Docker, você pode garantir que seu aplicativo seja executado de forma consistente, independentemente do ambiente em que está sendo implantado.

You can also see about this topic in [Installation Python](https://www.docker.com/)

## <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="15"/> Python

Python é uma linguagem de programação de alto nível conhecida por sua simplicidade e versatilidade. É amplamente utilizado em diversos campos, como desenvolvimento web, análise de dados, inteligência artificial e muito mais. Python possui uma comunidade grande e ativa que contribui continuamente para o seu desenvolvimento e oferece uma ampla gama de bibliotecas e frameworks. Sua legibilidade e facilidade de uso o tornam uma escolha popular entre os desenvolvedores, tanto para iniciantes quanto para programadores experientes.

You can also see about this topic in [Installation Python](https://www.python.org/)

## <img src="https://cdn.worldvectorlogo.com/logos/fastapi-1.svg" width="15"/> Fastapi

O FastAPI é um framework web de alto desempenho para construir APIs em Python. Ele é baseado no Starlette e utiliza a tipagem do Python 3.7+ para fornecer uma experiência de desenvolvimento rápida e eficiente. Com o FastAPI, é possível criar APIs assíncronas de forma simples e fácil, aproveitando ao máximo a velocidade e a produtividade do Python. Ele oferece recursos como geração automática de documentação interativa, validação de tipos de dados, suporte para autenticação e autorização, entre outros. O FastAPI é uma excelente escolha para desenvolver APIs modernas e escaláveis.

Você também pode ver sobre este tópico em [Installation FastApi](https://fastapi.tiangolo.com/)

# 🎯 Configuration 


### 1. Configurating Python
<!-- O Kpi Forecasting é um aplicativo baseado em um projeto Django que utilizou bibliotecas Python 3.10. Para mais detalhes você pode visitar [Repository kpi](https://gitsoft.softexpert.com/services/kpiforecast/). -->

```python
# Verificando a versão do projeto

python --version 
```

> Você pode receber este resultado

```python
> Python 3.10
```

```python
# Criando ambiente python

python -m venv env
```
<span>&#9888;</span>A etapa acima é a mais importante que será criada na base do projeto


```python
# Instalando as dependências necessárias

pip install -r ./docs/requirements.txt
```

Você poderá testar a aplicação antes de subir o container

```python
python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### Observações

> Após configurar o projeto, você poderá ver alguns arquivos como este:

- logs.log  - Este arquivo é gerado quando o servidor uvicorn está rodando
 
<br />

## 2. Configurating Docker

### 2.1 Dockerfile

Começaremos configurando o **Dockerfile** que é mais importante para a construção da aplicação, com os seguintes comandos que serão explicados linha por linha como no exemplo.

> Este arquivo será encontrado no caminho **container**

Configurando a versão do python no containers e definindo como basear

```Dockerfile
FROM python:3.10.12 as base
```

```Dockerfile
# Instalando bibliotecas virtualenv

RUN pip install virtualenv

# Configurando o virtualenv no container após a criação

RUN python -m venv env

# Executando o virtualenv com o comando bash

RUN /bin/bash -c "source /env/bin/activate"
```

```Dockerfile
# Criando a pasta que recebe a aplicação

WORKDIR /app

# Copiando os requisitos para o aplicativo

COPY ./container/requirements.txt /app/requirements.txt 

# Copiando o aplicativo para o containers

COPY ./src /app/
```

Executando a atualização do pip e instalando os requisitos

```Dockerfile
RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
```

Esta parte é mais importante, pois sem esta modificação nas bibliotecas a aplicação não roda com sucesso

> This files will be found in path: **container/files**

```Dockerfile
# Removendo o arquivo padrão da biblioteca  

RUN rm /usr/local/lib/python3.10/site-packages/pycaret/internal/pycaret_experiment/supervised_experiment.py

# Substituindo o arquivo modificado para dentro do container 

COPY ./container/files/supervised_experiment.py /usr/local/lib/python3.10/site-packages/pycaret/internal/pycaret_experiment/supervised_experiment.py
```

Ao final, é necessário executar a aplicação com o comando mostrado em Begin no início

```Dockerfile
CMD ["python", "-m", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

Logo em seguida, poderá construir o container e logo em seguida realizar os testes

```bash
docker build -t "Application name" "Dockefile path"  

# Ao final do processo, você poderá ver o container pronto para ser executado

# É necessário verificar todos os containers com o comando:

docker images -a
```
Pesquise seu container com o nome inicial, se tudo correu bem com o processo, você pode executar

```bash
docker run -d --name "container name" -p "listening port":"bound port" "container":latest

# Exemplo: docker run -d --name kpi -p 8000:8000 build-kpi:latest 
```

### 2.2 Docker Compose

Basicamente o arquivo **docker-compose.yml** é um arquivo para configuração do container, e você pode definir a rede, portas e serviços que estarão sendo executados no seu container, conforme a receita mostrada anteriormente.

```Docker
version: '3' 
services:
  fastapi:
    build: 
      dockerfile: ./container/Dockerfile 
      context: ./ 
    container_name: build-kpi 
    ports:
      - "8000:8000" 
    volumes:
      - .:/app
    restart: always 

```
Explique sobre atributos em **docker-compose.yml**

* **dockerfile**: Caminho para o Dockerfile
* **container_name**: Nome do containers, após a construção
* **ports**: Portas usadas em seu em seu container, dentre elas a porta de entrada e a porta de saída
* **restart**: Reiniciando seu container, caso haja alguma alteração no código

Finalmente você pode executar o seguinte comando:

> Se for executar a aplicação pela primeira vez

```bash
docker-compose up --build
```

Este comando cria o aplicativo com receita **Dockerfile**

> Ou você só pode executar o containers já construído

```bash
docker-compose up
```

<h4>Como excluir o containers</h4>

Você pode excluir o containers seguindo os passos abaixo

1. Listando todos os containers em execução, para obter o ID do containers

```bash
janela de encaixe ps -a
```

2. Depois de obter o containers, você precisará parar o containers antes de removê-lo

```bash
docker parar "container_id"
```

3. Finalmente você pode excluir o containers 

```bash
docker parar "container_id"
```
### Observações

Se deseja remover a imagem do container

```bash
docker rmi "container_id"
```

> Lembre-se que você só apaga o container, se não estiver sendo utilizado
