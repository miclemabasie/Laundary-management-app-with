FROM python:3.10.0-slim-buster

# set environment variables
ENV APP_HOME=/app
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
WORKDIR $APP_HOME


LABEL maintainer="miclemabasie3@gmail.com"
LABEL youtube="None"
LABEL description="Development Image for Laundary manage ment API"


ENV PYTHONDONTWRITEBYTECODE 1
# FOR DOCKER LOGS
ENV PYTHONUNBUFFERED = 1

# INSTALL DEPENDENCIES
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev \
    && apt-get install -y gettext \
    && apt-get install -y netcat gcc postgresql \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip


# installing requirements
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip intsll -r requirements.txt


# Entrypointfile specifies custom commands to run before container starts
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# first command to run when container starts
ENTRYPOINT [ "/entrypoint" ]
