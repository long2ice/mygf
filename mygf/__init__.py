from pymysqlreplication import BinLogStreamReader
from pymysqlreplication.row_event import DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent

from .sync import SyncLogPos, SyncCache

__version__ = '0.0.1'


class MyGf:
    _bin_log_stream = None
    _server_id = None

    @classmethod
    def init(
            cls,
            host='127.0.0.1',
            port: int = 3306,
            user='root',
            password=None,
            log_file=None,
            log_pos=None,
            only_schemas=None,
            only_tables=None,
            server_id=None
    ):
        cls._bin_log_stream = BinLogStreamReader(
            connection_settings=dict(
                host=host,
                port=port,
                user=user,
                password=password
            ),
            server_id=server_id,
            freeze_schema=True,
            only_events=[DeleteRowsEvent, UpdateRowsEvent, WriteRowsEvent, ],
            resume_stream=True,
            blocking=True,
            fail_on_table_metadata_unavailable=True,
            only_schemas=only_schemas,
            only_tables=only_tables,
            log_file=log_file,
            log_pos=log_pos
        )

    @classmethod
    def start_sync(cls):
        bin_log_stream = cls._bin_log_stream
        for binlog_event in bin_log_stream:
            schema = binlog_event.schema
            table = binlog_event.table
            log_pos = bin_log_stream.log_pos
            log_file = bin_log_stream.log_file
            SyncLogPos.set_log_pos_slave(log_file, log_pos)
            SyncCache.clean_cache(schema, table)


def run_forever(
        server_id,
        backend_cls,
        backend_kwargs,
        mysql_host,
        mysql_port,
        mysql_user,
        mysql_password,
        only_schemas,
        only_tables
):
    backend = backend_cls(**backend_kwargs)

    SyncCache.init(backend)
    SyncLogPos.init(backend, log_pos_prefix='mysql_binlog_pos', server_id=server_id)

    log_file, log_pos = SyncLogPos.get_log_pos()

    MyGf.init(
        host=mysql_host,
        port=mysql_port,
        user=mysql_user,
        password=mysql_password,
        log_file=log_file,
        log_pos=log_pos,
        only_schemas=only_schemas,
        only_tables=only_tables,
        server_id=server_id
    )

    MyGf.start_sync()
