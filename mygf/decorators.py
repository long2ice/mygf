import functools

from mygf import SyncCache


def register_sync(table, schema=None):
    """
    register cache sync
    :param schema:
    :param table:
    :return:
    """

    def wrapper(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            SyncCache.add_sync_key(schema or SyncCache.default_schema, table, f.compose_key(*args, **kwargs))
            return f(*args, **kwargs)

        return inner

    return wrapper
