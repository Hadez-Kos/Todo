FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY . .

COPY todo/req.txt app/req.txt

RUN apt-get update -y \
    && pip3 install --upgrade pip

RUN pip3 install psycopg2-binary

RUN pip3 install -r app/req.txt

CMD ["python3", "RunProject.py"]
