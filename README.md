# real-python-redis-series

This project was created to study redis in the 'real python' class.

# Class Site Links

## redis cache

- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Caching in Django With Redis](https://realpython.com/caching-in-django-with-redis/)
  - [github repo](https://github.com/realpython/django-redis-cache)

## redis queue

- [Redis Queue (RQ)](https://www.fullstackpython.com/redis-queue-rq.html)
- [django-rq](https://github.com/rq/django-rq)
  - [Django RQ: A Simple App That Provides Django integration For RQ](https://morioh.com/p/1489e396a898)
  - [Advanced Django-RQ Example](https://stuartm.com/2020/05/advanced-django-rq-example/)
- [django-rq-scheduler : A database backed job scheduler for Django RQ with Django](https://snyk.io/advisor/python/django-rq-scheduler#package-footer)
- [Asynchronous tasks in Django with Django Q](https://www.valentinog.com/blog/django-q/)
- [How to Run Your First Task with RQ, Redis, and Python](https://www.twilio.com/blog/first-task-rq-redis-python)
- [RQ official site](https://python-rq.org/docs/)

## redis pub/sub

- [eng-ver : Hands-on with Redis and Django](https://enlear.academy/hands-on-with-redis-and-django-ed7df9104343)
  - [kor-ver : Django Redis - caching, scheduling (task), pub/sub message que](https://velog.io/@qlgks1/Django-Redis-caching-scheduling-task-messaging-celery-async-worker)
- [how-to-use-redis-for-caching-and-pub-sub-in-python](https://betterprogramming.pub/how-to-use-redis-for-caching-and-pub-sub-in-python-3851174f9fb0)
- [redis publish / subscribe python example](https://blog.naver.com/PostView.naver?blogId=pareko&logNo=222528721348&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView)

## redis pub/sub

- [Asynchronous Tasks With Django and Celery](https://realpython.com/asynchronous-tasks-with-django-and-celery/)

# Project Environment

- Windows version of redis-server download
  - [zkteco-home/redis-windows](https://github.com/zkteco-home/redis-windows)
  - [tporadowski / redis](https://github.com/tporadowski/redis)
- [Registering with Services in Windows - korean version](https://gerger.tistory.com/143)

# How to Use Redis With Python

### Project Information

- project name : how-to-use-redis
- blacklist ip detect reference :
  - [Better Rate Limiting With Redis Sorted Sets](https://engineering.classdojo.com/blog/2015/02/06/rolling-rate-limiter/)
  - book [Redis in Action 1st Edition](https://www.amazon.com/dp/1617290858/?tag=devdetailpage02-20)
  - study more :
    - [server-side Lua scripting](https://redis.io/commands/eval/)
    - [Scaling with Redis Cluster](https://redis.io/docs/management/scaling/)
    - [Redis replication](https://redis.io/docs/management/replication/)
    - [Why RESP3 will be the only protocol supported by Redis 6](http://antirez.com/news/125)
- project name : caching-in-django-with-redis
  - prepare : python manage.py loaddata cookbook/fixtures/cookbook.json

### Load Test

#### locust

- install :
  - pip install locust
- work set : create file as locustfile.py in 'caching-in-django-with-redis' project
