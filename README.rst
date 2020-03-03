========
mygf
========

Girlfriend of MySQL(Clean up cache with MySQL binlog,based on the cache framework `ring <https://github.com/youknowone/ring>`_).

Installation
============

.. code-block:: bash

    pip3 install mygf

Cache
==========

Just use ``register_sync`` as decorator of ``ring``,must call ``SyncCache.init`` first:

.. code-block:: python

    import aioredis
    import asynctest

    import ring
    from asynctest import TestCase

    from mygf import SyncCache
    from mygf.backends.redis import RedisBackend
    from mygf.decorators import register_sync

    backend = RedisBackend()

    SyncCache.init(backend)

    redis = aioredis.create_redis('redis://127.0.0.1:6379', encoding='utf8')


    @register_sync('test', 'test')
    @ring.aioredis(redis, expire=30)
    async def test():
        return 1


    class TestSync(TestCase):

        async def test_sync_cache(self):
            ret = await test()
            self.assertEqual(int(ret), 1)


    if __name__ == '__main__':
        asynctest.main()


Cleanup Cache
=============

A new file maybe named ``main.py``,then hung up use ``python main.py``:

.. code-block:: python

    from mygf import run_forever
    from mygf.backends.redis import RedisBackend

    if __name__ == '__main__':
        run_forever(
            server_id=101,
            backend_cls=RedisBackend,
            backend_kwargs=dict(host='127.0.0.1', port=6379, password=None, db=0),
            mysql_host='127.0.0.1',
            mysql_port=3306,
            mysql_user='root',
            mysql_password='123456',
            only_schemas=['test'],
            only_tables=['test']
        )

ThanksTo
========
* `ring <https://github.com/youknowone/ring>`_,a nice python cache framework.