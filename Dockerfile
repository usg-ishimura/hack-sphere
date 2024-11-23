# syntax=docker/dockerfile:1

FROM ubuntu:22.04

WORKDIR /hack-sphere

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    docker.io \
    docker-compose-v2

RUN pip3 install -r requirements.txt

COPY . .

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

CMD ["python3", "app.py"]
