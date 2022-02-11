<h1> Aula 0 - Prática </h1>

<h3> 
    Ambiente local no Docker utilizando Pyspark e Jupyter Notebook 
</h3>
    <h4>
        O que será necessário para montar esse ambiente?
    </h4>

1. Instalação do git para clonar o projeto
    - Tutorial para Windows [Git para Windows](https://www.atlassian.com/git/tutorials/install-git)
    - Tutorial para Linux [Git para Linux](https://www.atlassian.com/git/tutorials/install-git)
    - Tutorial para MacOS [Git para MacOS](https://www.atlassian.com/git/tutorials/install-git)
2. Instalação do Docker para deployment local dos containers
    - Tutorial para Windows [Docker Desktop para Windows](https://docs.docker.com/desktop/windows/install/)
    - Tutorial para Linux [Docker para Linux](https://docs.docker.com/engine/install/ubuntu/)
    - Tutorial para MacOS [Docker Desktop para MacOS](https://docs.docker.com/desktop/mac/install/)
3. Criar um arquivo .env com as seguintes variaveis conforme apresentado em aula
    ```
    NOTEBOOKS_PATH
    DATA_PATH
    ```
4. Executar os seguintes comandos no terminal
    ```- docker-compose up -d```
5. Acessar a url no seu navegador com o endereço 
    ```0.0.0.0:8888```