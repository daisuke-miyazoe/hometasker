FROM python:3.10

RUN mkdir /hometasker
WORKDIR /hometasker
COPY requirements.txt /hometasker/ 
RUN pip install -r requirements.txt
COPY . /hometasker/