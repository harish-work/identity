# Identity

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/harish-work/identity.git
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ virtualenv identify-env
$ source env/bin/activate
```
Then install the dependencies:
```sh
(identify-env)$ pip install -r requirements.txt
```
## Getting Started
```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Screenshots
1. Create Identify.
![Screenshot 2024-06-09 103942](https://github.com/harish-work/identity/assets/163814679/ae917659-f8e9-4351-96b4-435d8d9de269)


2.Get all Identify.
!note to pass the token the header.
![image](https://github.com/harish-work/identity/assets/163814679/41bb7026-5ae6-4bc9-a89b-765628970616)



## Using Docker
### Docker build
```sh
$ docker build -t identity .
```
### Docker Run
```sh
$ docker run -p 9000:8000 imageid
```

