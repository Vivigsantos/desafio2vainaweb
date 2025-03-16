Desafio Api/flask/SQL

Uma breve descrição do projeto, explicando sua finalidade e funcionalidades principais.

Tecnologias Utilizadas

Python

Flask

REST Client para VS Code (test.http)

Como Executar o Projeto

1. Clonar o Repositório

 git clone https://github.com/seu-usuario/seu-repositorio.git
 cd seu-repositorio

2. Criar um Ambiente Virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3. Instalar Dependências

pip install -r requirements.txt

4. Executar a API

python nome_do_arquivo.py  # Substitua pelo nome do arquivo principal

A API estará rodando em http://127.0.0.1:5000/

Como Testar a API

1. Instalar a Extensão REST Client (VS Code)

Se ainda não tiver a extensão, instale REST Client.

2. Criar o Arquivo test.http

Crie um arquivo test.http na raiz do projeto e adicione as requisições para testar a API, por exemplo:

GET http://127.0.0.1:5000/

3. Executar os Testes

Abra o arquivo test.http no VS Code e clique no botão "Send Request" para testar a API.

Contribuição

Se quiser contribuir com o projeto, siga os passos:

Faça um fork do repositório.

Crie uma nova branch (git checkout -b minha-feature).

Faça as alterações e commit (git commit -m 'Minha nova feature').

Faça um push para a branch (git push origin minha-feature).

Abra um Pull Request.
