# D3Builder

The current project presents a web platform to store and share _Builds_ for the famous videogame **Diablo 3**.

This project is made out of two main components:
- Front-End: Made with **Angular Framework**.
- Back-End: Made with **Django Framework**.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Use `git clone https://github.com/arceus6666/d3builder.git` to get a copy of the project.

### Prerequisites

What things you need to install the software and how to install them.


### Windows Installation

- MongoDB
  + [Download MongoDB](https://www.mongodb.com/download-center/community)
- Python
  + [Download Python](https://www.python.org/downloads/)
- Virtual Environment
  + `> py -m pip install virtualenvwrapper-win`
  + `> mkvirtualenv d3builderenv`
  + `> workon d3builderenv`
- Django Framework
  + `> py -m pip install Django`
- Djongo MongoDB for Django
  + `> py -m pip install djongo`
- Django Rest Framework
  + `> py -m pip install djangorestframework`
- Django CORS
  + `> py -m pip install django-cors-headers`
- NodeJS
  + [Download NodeJS](https://nodejs.org/en/download/)
- Angular CLI
  + `> npm install -g @angular/cli`


### Linux Installation
- MongoDB
  + `> wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -`
    + If you get an error use `> sudo apt-get install gnupg` and retry
  + `> echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list`
  + `> sudo apt-get update`
  + `> sudo apt-get install -y mongodb-org`
  + `> sudo systemctl start mongod`
- Python
  + `> sudo apt-get install python3`
  + `> sudo apt-get install python3-pip`
- Virtual Environment
  + `> sudo pip3 install virtualenv`
  + `> virtualenv d3builderenv`
  + `> source d3builderenv/bin/activate`
- Django Framework
  + `> pip3 install Django`
- Djongo MongoDB for Django
  + `> pip3 install djongo`
- Django Rest Framework
  + `> pip3 install djangorestframework`
- Django CORS
  + `> pip3 install django-cors-headers`
- NodeJS
  + `> sudo apt-get install curl`
  + `> curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -`
  + `> sudo apt-get install nodejs`
- Angular CLI
  + `> npm install -g @angular/cli`

### Creating database
For this step there is two options.

Database name is **`d3builder`**.
- Creating database from terminal.
- Creating database from GUI software, like [Robo3T](https://studio3t.com/download/).


### Installing

A step by step series of examples that tell you how to get a development env running

Installing Angular dependencies.

```
./d3builder>cd front
./d3builder/front>npm i
```

Installing Django dependencies.

```
./d3builder>cd back
./d3builder/back>py mygrate.py makemigrations
./d3builder/back>py mygrate.py migrate
```

Running Angular project.

```
./d3builder>cd front
./d3builder/front>ng serve
```

Running Django project.

```
./d3builder>cd back
./d3builder/back>py mygrate.py runserver
```

Accesing Angular page.

`http://localhost:4200/`

Accesing Django api.

`http://localhost:8000/api/`

## Built With

* [Angular](https://angular.io/) - The Front-End framework used
* [Django](https://www.djangoproject.com/) - The Back-End framework used
* [MongoDB](https://www.mongodb.com/) - Used for DataBase


## Authors

* **Daniel Mendoza**
  - Github: [arceus6666](https://github.com/arceus6666)
  - E-mail: arceus6666@hotmail.com

* **Rosa Zambrana**
  - Github: [rosamayte](https://github.com/rosamayte)
  - E-mail: rosmayza798@gmail.com
* **Sergio Bellott**
  - Github: [SergiusxD](https://github.com/SergiusxD)
  - E-mail: sbellott@hotmail.com
## License

This project is licensed under the [ISC License](https://www.isc.org/licenses/).
