FROM python:slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential curl software-properties-common git

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY src src

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

ENTRYPOINT ["streamlit", "run", "src/main.py", "--server.port=8080", "--server.address=0.0.0.0"]
