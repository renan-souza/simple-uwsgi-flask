FROM python:3.8

COPY . /app
WORKDIR /app
RUN python3.8 -m pip install --upgrade pip
RUN python3.8 -m pip install -r /app/requirements.txt

CMD ["/bin/bash", "-c", "exec uwsgi --ini /app/uwsgi.ini"]
