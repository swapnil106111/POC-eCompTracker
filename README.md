# POC-eCompTracker

eCompTracker is basically used for managing compliance.

Installation steps for ubuntu:

`sudo apt-get update`

`sudo apt-get install docker.io`


To check version of installed docker:

`sudo docker --version`

To start the docker service:

`sudo service docker start`


For more information, you can go here [https://docs.docker.com/get-docker/](Docker)

Install docker-compose:

`pip install -U docker-compose`

If everything installs successfully then run below commands:

`git clone https://github.com/swapnil106111/POC-eCompTracker.git`

`cd POC-eCompTracker`

`sudo docker build .`

`sudo docker-compose up`

Access url on chrome:

`localhost:8000`

If you are facing any issue in creating superuser then go to django container.
