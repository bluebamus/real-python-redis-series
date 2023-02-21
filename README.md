# real-python-redis-series

This project was created to study redis in the 'real python' class.

# Class Site Links

## redis cache

- [How to Use Redis With Python](https://realpython.com/python-redis/)
- [Caching in Django With Redis](https://realpython.com/caching-in-django-with-redis/)
  - [github repo](https://github.com/realpython/django-redis-cache)

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
