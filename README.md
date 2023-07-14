# Gerência e Configuração de Mudanças
### Sobre
Esse projeto tem em vista servir de base para a disciplina de Gerência e Configuração de Mudanças (DIM0517)

O projeto é baseado em python Django e consiste em um sistema bancário simples

# Para rodar o projeto

É necessário a versão 3.8 do Python ou maior e a do Django 4.2.
Para facilitar foi disponibilizado um pyproject.toml e um poetry.lock
Dessa forma, você consegue rodar o projeto utilizando o poetry para instalá-lo siga a documentação oficial:
https://python-poetry.org/docs/

É possível rodar o projeto com os comandos:

```
poetry lock
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py runserver
```

# Para rodar os testes unitários

Após ter o projeto rodando na sua maquina basta utilizar o comando:

```
poetry run python manage.py test
```

### Rotas:
As rotas de contas desenvolvidas são essas abaixo, cada uma tem um template HTML para criar, verificar, debitar, transferir e render entre contas:

![image](https://github.com/paulovanzo/gcm-api/assets/53716440/8bff8360-052b-4bce-a3c1-86ff44ec3b58)

GitFlow:

![branches1](https://raw.githubusercontent.com/paulovanzo/gcm-api/main/gitkraken1.png)

![branches2](https://raw.githubusercontent.com/paulovanzo/gcm-api/main/gitkraken2.png)


# Autores
[Paulo Vanzolini Moura da Silva](https://github.com/paulovanzo),
[Giovanna Karla de Macedo Félix](https://github.com/giooogk),
[José de Sousa Silva Filho](https://github.com/zedsousa)
