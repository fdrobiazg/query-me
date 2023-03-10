FROM python:3.8-slim-buster

WORKDIR /query-me

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python3", "-u", "main.py" ]