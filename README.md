# django-musics

Tuto Django - Vue génériques - Bootstrap - Bootswatch

Django example project with bootstrap4 templates (Bootswatch) , Generic Views, etc.

## Installation

- create a virtualenv : `virtualenv -p python3 venv`
- activate : `source venv/bin/activate``
- install  static dependencies :
    - `cd static ` (at root level)
    - `npm i jquery popper.js bootstrap bootswatch @fortawesome/fontawesome-free`
    - or just at root level : `yarn new install`

## Migrations and data

- migrations : `./manage.py makemigrations` `./manage.py migrate`
- load initial data : `./manage.py loaddata initial_musiques_data.json`

## Lancer le serveur


`./manage.py runserver`


## ou simply ... with gitpod 


[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/roza/django-musics)
