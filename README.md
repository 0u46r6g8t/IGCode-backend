# DataLAB - Kpi Forecast

<description>

## Índice

1. Instalação
2. Estrutura do projeto
3. Constribuição
4. Contato

## 1. Instalação

Para instalar o projeto será necessário configurar um ambiente de desenvolvimento, sendo necessário ter instalado em sua máquina as seguintes tecnologias:

- Docker
- Python3.10

Ao instalar as tecnologias acima, abra o arquivo no seguinte caminho:

> **Ambiente:** docs/environments.md

> **Comandos úteis:** docs/commands.md

## 2. Estrutura do projeto

```bash
backend/
├── container/          # Utilitários para execução do container
│   └── requirements.txt    # Dependências do projeto
│
├── docs/               # Arquivos de documentação
│
├── src/                # Pasta princípal do projeto
│   ├── classes/        # Classes com as regras de negócio 
│   ├── config/         # Configurações da API
│   ├── enums/          # Enums configurados
│   ├── models/         # Modelos de interfaces 
│   ├── router/         # Rotas configuradas
│   ├── utils/          # Utilitários do projeto
│   └── main.py         # Arquivo principal
│
├── README.md           # Documento de apresentação
├── Dockerfile          # Configuração do container
├── docker-compose.yml  # Configuração do composer do docker
├── .gitlab-ci.yml      # Configuração do deploy do projeto 
├── .dockerignore       # Arquivos ignorados pelo docker
└── .gitignore          # Arquivos a serem ignorados no controle de versão
```

## 3. Contribuição

Contribuições são bem-vindas! Para contribuir com o projeto, siga as etapas abaixo:

1. Crie uma nova branch a partir da branch **dev**. 

```bash
git checkout -b CNT-qualquer
``` 

2. Realize um commit das suas alterações

```bash
git commit -m "Descrição da sua alteração"
```

3. Envie as suas alterações para o repositório remoto

```bash
git push origin 'minha branch'
```

## 4. Contato

Se você tiver alguma dúvida, sugestão ou feedback sobre o projeto, fique à vontade para entrar em contato! Aqui estão algumas formas de entrar em contato:


- **Gustavo Silva:** [@Qu13r3g4t@](mailto:gustavo.s.quieregatog@gmail.com)
