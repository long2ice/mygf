from mygf import run_forever

if __name__ == '__main__':
    run_forever(
        server_id=101,
        backend_cls='mygf.backends.redis.RedisBackend',
        backend_kwargs=dict(host='127.0.0.1', port=6379, password=None, db=0),
        mysql_host='127.0.0.1',
        mysql_port=3306,
        mysql_user='root',
        mysql_password='123456',
        only_schemas=['test'],
        only_tables=['test']
    )
