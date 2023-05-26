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

# Autores
[Paulo Vanzolini Moura da Silva](https://github.com/paulovanzo)
[Giovanna Karla de Macedo Félix](https://github.com/giooogk)
[José de Sousa Silva Filho](https://github.com/zedsousa)