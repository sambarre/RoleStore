# Dockerfile, Image, Container 
FROM python:3.12.0a4-slim-bullseye

ADD . /app

RUN pip install discord responses python-dotenv

CMD [ "python", "./app/main.py"]