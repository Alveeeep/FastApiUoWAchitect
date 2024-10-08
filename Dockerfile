FROM python:3.10

RUN mkdir /fastapi_kitties

WORKDIR /fastapi_kitties

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh