FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3-pip

WORKDIR /app

COPY . /app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["run.py"]


