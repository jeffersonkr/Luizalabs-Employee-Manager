[![Build Status](https://travis-ci.com/jeffersonkr/Luizalabs-Employee-Manager.svg?branch=master)](https://travis-ci.com/jeffersonkr/Luizalabs-Employee-Manager)

Python Django project for management of Luiza Labs's employees.
==================================================================

### The Problem:
Luizalabs' team is growing every month and now we need to have some application to manage
employees' information, such as name, e-mail and department. As any application written at
Luizalabs, it must have an API to allow integrations

### Solution:
Using Python 3.6 and framework Django was created an solution with REST API and Django Admin.

### Instalation guide on local machine:
Considering python3 and pip is already installed, we should use these bellow step:
 - git clone repository url
 - go to project directory
 - pip install -r requirements.txt
 - python manage.py createsuperuser
    - Here we will make an user to access administration site.
 - python manage.py runserver

### Using admin site on local machine:
 - Open an browser and go to http://localhost:8000.
 - Insert login and password registered on instalation guide.

### API End-Points:
 - Get all employees ` GET : /employee/ `
 - Get employee ` GET : /employee/<id> `

### Using API with curl:
 - Open shell and type bellow command
 - `curl -H "Content-Type: application/javascript" http://localhost:8000/employee/`
 - or directly access url in browser.