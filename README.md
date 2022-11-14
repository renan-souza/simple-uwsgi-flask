# Simple-uwsgi-flask

### uWSGI server: Docker Build and Run

```bash
$> docker build -t simple_uwsgi_flask .
```

```bash
$> docker run --memory="8g" --cpus="5.0" -v `pwd`:/app -p 5000:5000 -it simple_uwsgi_flask
```

