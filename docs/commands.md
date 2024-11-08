## Configuração

Neste documento será possível encontrar uma lista de comandos que podem facilitar a vida durante o desenvolvimento ou o teste do projeto.

OBS: Os comandos abaixo devem ser adicionados ao bashrc para funcionar corretamente.

```bash
# Comando do docker

# Visualizar todos os contêineres no ambiente 
alias dl="docker ps -a"

# Visualizar todas as imagens 
alias dli="docker images -a "

# Derrubar a execução de um serviço ativo
alias dpd="docker-compose down"

# Derrubar a execução, e remover qualquer dependência do serviço
alias dprd="docker-compose down --remove-orphans"

# Construir um serviço (instalar todas as dependências)
# Executar somente a primeira vez
alias dpub="docker-compose up --build"

# Subir um serviço que já foi construído
alias dpu="docker-compose up"

# Necessário adicionar um argumento indicando qual é a imagem (id)
alias drmi="docker rmi "
```

