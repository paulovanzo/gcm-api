FROM python:3.11-slim-buster as dep

RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install poetry virtualenv \
    && pip3 install --upgrade setuptools

RUN mkdir /srv/app

COPY . /srv/app/

COPY pyproject.toml poetry.lock /srv/app/

FROM dep as build

WORKDIR /srv/app

RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev

FROM build as app

ARG DJANGO_SECRET_KEY
ENV SECRET_KEY ${DJANGO_SECRET_KEY}

RUN groupadd -r gcm \
    && useradd -r -g gcm gcm \ 
    && chown gcm.gcm -R /srv/app/

USER gcm

EXPOSE 8080

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate && gunicorn gcm.wsgi:application -b 127.0.0.1:8080"]