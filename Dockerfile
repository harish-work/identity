FROM python:3.12.0

WORKDIR  /bites


COPY requirements.txt /bites
RUN pip install -r requirements.txt


COPY . /bites

RUN python manage.py makemigrations
RUN python manage.py migrate

ENTRYPOINT ["python"]
CMD ["manage.py","runserver","0.0.0.0:8000"]

