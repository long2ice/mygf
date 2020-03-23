import logging

from mygf.backends import BaseBackend

logger = logging.getLogger('mygf.sync')


class SyncLogPos:
    _backend = None
    _key = None

    @classmethod
    def init(cls, backend: BaseBackend, log_pos_prefix=None, server_id=None):
        cls.server_id = server_id
        cls.log_pos_prefix = log_pos_prefix
        cls._key = f'{log_pos_prefix}:{server_id}'
        cls._backend = backend

    @classmethod
    def set_log_pos_slave(cls, log_file, log_pos):
        cls._backend.hmset(cls._key, {
            'log_pos': log_pos,
            'log_file': log_file
        })

    @classmethod
    def get_log_pos(cls):
        log_position = cls._backend.hgetall(cls._key) or {}
        return log_position.get('log_file'), int(log_position.get('log_pos'))


class SyncCache:
    _backend = None
    _prefix = 'sync_cache'
    default_schema = None

    @classmethod
    def init(cls, backend: BaseBackend, default_schema=None):
        cls._backend = backend
        cls.default_schema = default_schema

    @classmethod
    def _get_sync_key(cls, schema, table):
        return f'{cls._prefix}:{schema}:{table}'

    @classmethod
    def add_sync_key(cls, schema, table, key):
        cache_key = cls._get_sync_key(schema, table)
        cls._backend.sadd(cache_key, key)

    @classmethod
    def clean_cache(cls, schema, table, ):
        cache_key = cls._get_sync_key(schema, table)
        keys = cls._backend.smembers(cache_key)
        if keys:
            cls._backend.delete(*keys)
            logger.info(f'成功清除缓存keys：{keys}')

    @classmethod
    def clean_sync_key(cls, schema, table):
        cache_key = cls._get_sync_key(schema, table)
        cls._backend.delete(cache_key, )
