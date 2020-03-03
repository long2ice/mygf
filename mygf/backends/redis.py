import redis

from mygf.backends import BaseBackend


class RedisBackend(BaseBackend):

    def __init__(self, host='127.0.0.1', port=6379, password=None, db=0):
        pool = redis.ConnectionPool(host=host, port=port, db=db, password=password, decode_responses=True)
        self.ins = redis.StrictRedis(connection_pool=pool)

    def sadd(self, name, values):
        return self.ins.sadd(name, values)

    def smembers(self, name):
        return self.ins.smembers(name)

    def delete(self, *names):
        return self.ins.delete(*names)

    def hmset(self, name, keys, *args):
        return self.ins.hmget(name, keys, *args)

    def hgetall(self, name):
        return self.ins.hgetall(name)

