# Django session clustering sample

## Reference

- https://docs.djangoproject.com/en/4.1/topics/http/sessions/
- https://apirobot.me/posts/tale-about-redis-and-sessions-in-django
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/ebextensions-optionsettings.html
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

## Setup environment
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## Redis (local)
```
docker network create my-net
docker run -p 6379:6379 --net my-net --name my-redis -d redis:latest
docker run -it --net my-net --rm redis redis-cli -h my-redis
```

## Run Django (local)
```
# (local) run server
python manage.py runserver
# (local) run django via container
docker run -p 8000:8000 --net my-net --name my-django --env-file ./env.list -d cloudacode/django:v0.1.3
```

## Deploy to ElasticBeanstalk

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html

```
# Set platform as python3.7
# https://stackoverflow.com/questions/66380006/django-deterministic-true-requires-sqlite-3-8-3-or-higher-upon-running-python#answer-70408040
eb init -p python-3.7 django-session

# Deploy elasticbeanstalk
eb create django-env -r ap-northeast-2 --vpc.id <vpc-id> --vpc.elbsubnets <subnet-01,subnet-02> --vpc.ec2subnets <subnet-01,subnet-02> --vpc.publicip --vpc.elbpublic
```

## Deploy Docker to ElasticBeanstalk

```
$ cd configuration/
$ zip -r configuration.zip ./
    adding: Dockerrun.aws.json (deflated 30%)
    adding: .ebextensions/ (stored 0%)
    adding: .ebextensions/environmentvariables.config (deflated 26%)
```
