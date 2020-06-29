FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev  -y
RUN pip3 install -r requirements.txt

COPY . /code/
CMD ["python","authentication/manage.py","migrate"]