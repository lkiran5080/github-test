import os
import redis

#r = redis.Redis()


if __name__ == '__main__':
    r = redis.from_url(os.environ.get('REDIS_URI'))
    print(r.ping())
