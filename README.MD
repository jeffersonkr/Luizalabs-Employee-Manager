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
 - Get employee ` GET : /employee/<id>/ `
 - Add employee ` POST : /employee/ `
 - Delete employee ` DELETE : /employee/<id>/ `
 - Update employee ` PUT : /employee/<id>/ `
 - Get Access Token ` GET : /api/token/ `
 - Refresh Access Token ` GET : /api/token/refresh/ `

### Using API with curl:
For Delete and PUT methods you should have a token.<br>
 - department tags `E: E-commerce`, `M : Mobile`, `A: Architeture`.

 - getting a token : `curl -X POST -d "username=<username>&password=<password>" http://localhost:8000/api/token/`
 - refreshing a token: `curl -X POST -H "Content-Type: application/json" -d '{"refresh":"<access-token>"}' http://localhost:8000/api/token/refresh/`
 - get all employees: `curl -X GET -H "Content-Type: application/javascript" http://localhost:8000/employee/`
 - get an employee : `curl -X GET -H "Content-Type: application/javascript" http://localhost:8000/employee/<id-employee>/ `
 - create employee : `curl -X POST http://localhost:8000/employee/ -H "Content-Type: application/json" -d '{"name": "<name>", "email": "<email>", "department": "<department tag>"}' `
 - delete an employee : `curl -X DELETE -H "Authorization: Bearer <access-token>" -H "Content-Type: application/javascript" http://localhost:8000/employee/<id-employee>/ `
 - update an employee : `curl -X PUT -H "Authorization: Bearer <access-token>" http://localhost:8000/employee/<id-employee>/ -H "Content-Type: application/json"  -d '{"name": "<name>", "email": "<email>", "department": "<department-tag>"}' `

