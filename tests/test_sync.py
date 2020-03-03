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
