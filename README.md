# Django session clustering sample

## Reference

https://docs.djangoproject.com/en/4.1/topics/http/sessions/
https://apirobot.me/posts/tale-about-redis-and-sessions-in-django

## Setup environment
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Redis (container)
```
docker network create my-net
docker run -p 6379:6379 --net my-net --name my-redis -d redis:latest
docker run -it --net my-net --rm redis redis-cli -h my-redis
```

## Run Django
```
# (local) run server
python manage.py runserver
# (local) run django via container
docker run -p 8000:8000 --net my-net --name my-django --env-file ./env.list -d cloudacode/django:v0.1.3
```
