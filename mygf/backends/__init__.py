import abc


class BaseBackend:
    @abc.abstractmethod
    def sadd(self, name, values):
        raise NotImplementedError

    @abc.abstractmethod
    def smembers(self, name):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, *names):
        raise NotImplementedError

    @abc.abstractmethod
    def hmset(self, name, mapping):
        raise NotImplementedError

    @abc.abstractmethod
    def hgetall(self, name):
        raise NotImplementedError
