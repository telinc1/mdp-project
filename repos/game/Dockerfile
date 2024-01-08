FROM python:slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential curl software-properties-common git

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY src src

ENTRYPOINT ["python3", "src/main.py"]
