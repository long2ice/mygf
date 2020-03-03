import functools

from mygf import SyncCache


def register_sync(schema, table):
    """
    register cache sync
    :param schema:
    :param table:
    :return:
    """

    def wrapper(f):
        @functools.wraps(f)
        def inner(*args, **kwargs):
            SyncCache.add_sync_key(schema, table, f.compose_key())
            return f(*args, **kwargs)

        return inner

    return wrapper
