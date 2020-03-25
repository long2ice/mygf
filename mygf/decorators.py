import functools

from mygf import SyncCache


def register_sync(*tables, schema=None):
    """
    register cache sync
    :param schema:
    :param tables:
    :return:
    """

    def wrapper(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            for table in tables:
                SyncCache.add_sync_key(schema or SyncCache.default_schema, table, f.compose_key(*args, **kwargs))
            return f(*args, **kwargs)

        return inner

    return wrapper
